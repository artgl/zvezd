#include <SoftwareSerial.h>

int ibus_pin = 2;
int unused_pin = 13;

struct IBusSensor
{
  byte type;
  unsigned int data;
};

IBusSensor sensors[] = {{0, 8}, {0, 9}};
int sensors_count = sizeof(sensors)/sizeof(sensors[0]);

byte hello_request[]  = {0x04,0x81};
byte type_request[]   = {0x04,0x91};
byte data_request[]   = {0x04,0xa1};
byte hello_response[] = {0x04,0x81};
byte type_response[]  = {0x06,0x91,0x00,0x02};
byte data_response[]  = {0x06,0xa1,0x00,0x00};

byte* checksum(byte *msg, int msg_len)
{
  static byte res[2];
  unsigned int checksum = 0xffff;
  for (int i = 0; i < msg_len; i++)
    checksum -= msg[i];

  res[0] = 0xff & checksum;
  res[1] = 0xff & (checksum >> 8);

  return res;
}

void sendMsg(byte *msg, int msg_len)
{
  SoftwareSerial ss(unused_pin, ibus_pin); // RX, TX  
  ss.begin(115200);
  ss.write(msg, msg_len);
  ss.write(checksum(msg, msg_len), 2);
}

void setAddr(byte *msg, byte addr)
{
  msg[1] = 0xf0 & msg[1] | 0x0f & addr;
}

void setType(byte *msg, byte type)
{
  msg[2] = type;
}

void setData(byte *msg, unsigned int data)
{
  msg[2] = 0xff & data;
  msg[3] = 0xff & (data >> 8);
}

void processOnePacket()
{
  SoftwareSerial ss(ibus_pin, unused_pin); // RX, TX  
  ss.begin(115200);
  
  byte buf[4];
  int c = 0;

  while (c < 4)
  {
    if (ss.available())
    {
      byte b = ss.read();
      if (c == 0 && b != 0x04)
        continue;
      buf[c++] = b;
    }
  }

  for (int i = 0; i < sensors_count; i++)
  {
    setAddr(hello_request, i + 1);
    setAddr(type_request, i + 1);
    setAddr(data_request, i + 1);
    setAddr(hello_response, i + 1);
    setAddr(type_response, i + 1);
    setAddr(data_response, i + 1);
    setType(type_response, sensors[i].type);
    setData(data_response, sensors[i].data);
        
    if (0 == memcmp(buf, hello_request, sizeof(hello_request)))
    {
      Serial.print("got hello request for sensor "); Serial.println(i + 1);
      sendMsg(hello_response, sizeof(hello_response));
      Serial.print("hello response sent for sensor "); Serial.println(i + 1);
      break;
    }  
    if (0 == memcmp(buf, type_request, sizeof(type_request)))
    {
      Serial.print("got type request for sensor "); Serial.println(i + 1);
      sendMsg(type_response, sizeof(type_response)); 
      Serial.print("type response sent for sensor "); Serial.println(i + 1); 
      break;
    }    
    if (0 == memcmp(buf, data_request, sizeof(data_request)))
    {
      Serial.print("got data request for sensor "); Serial.println(i + 1);
      sendMsg(data_response, sizeof(data_response));
      Serial.print("data response sent for sensor "); Serial.println(i + 1); 
      break;
    }
  }
}

void IBusInit()
{
  // We need to wait for hello and type requests for all N sensors,
  // so we should process first N * 2 packets. Here we process N * 4
  // packets to be absolutely sure and avoid possible receive errors
  for (int i = 0; i < sensors_count * 4; i++)
    processOnePacket();
}



void setup()
{
  Serial.begin(115200);
  sensors[1].type = 1;
  IBusInit();
}

void loop()
{
  sensors[0].data = millis() / 1000;
  sensors[1].data = millis() / 1000 + 400;
  processOnePacket();
  delay(5);
}
