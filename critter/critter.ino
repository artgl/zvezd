#include "Servo.h"

Servo ser1;
Servo ser2;
Servo ser3;
Servo ser4;

void setup() {
  Serial.begin(9600);
  // put your setup code here, to run once:

  ser1.write(90);
  ser2.write(90);
  ser3.write(90);
  ser4.write(90);

  ser1.attach(9);
  ser2.attach(10);
  ser3.attach(11);
  ser4.attach(12);

  Serial.println("Hello");
}

int from_serial = 0;
char *forward = "a130c030b150d030a030c140b030d150";
int pos = 0;

//   a030c140b150d030a140c030b030d150
//   a030c140b150d030a140c030b030d150

void loop() {
  // put your main code here, to run repeatedly:

  int b1, b2, b3, b4;
  if (from_serial)
  {
      b1 = Serial.read();
      while (b1 == -1) b1 = Serial.read();

      b2 = Serial.read();
      while (b2 == -1) b2 = Serial.read();
  
      b3 = Serial.read();
      while (b3 == -1) b3 = Serial.read();
  
      b4 = Serial.read();
      while (b4 == -1) b4 = Serial.read();
  }
  else
  {
      b1 = forward[pos + 0];
      b2 = forward[pos + 1];
      b3 = forward[pos + 2];
      b4 = forward[pos + 3];
      if ((pos + 4) < strlen(forward))
      {
          pos = pos + 4;
      }
      else
      {
          pos = 0;
      }
  }
  
  int grad = (b2 - '0') * 100 + (b3 - '0') * 10 + (b4 - '0');

  Serial.println((char) b1);
  Serial.println(grad);

  

  Servo* ser = NULL;

  if (b1 == 'a')
  {
      ser = &ser1;
  } 
  if (b1 == 'b')
  {
      ser = &ser2;
  }
  if (b1 == 'c')
  {
      ser = &ser3;
  }
  if (b1 == 'd')
  {
      ser = &ser4;
  }
  if (b1 == 'z')
  {
      delay(grad);  
  }
  
  if (ser)
  {
      int prev_grad = ser->read();
      int i;
      if (grad > prev_grad)
      {
          for (i = prev_grad; i <= grad; i++)
          {
              ser->write(i);
              delay(5);
          }
      }
      else
      {
          for (i = prev_grad; i >= grad; i--)
          {
              ser->write(i);
              delay(2);
          }
      }
    }  
}
