#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

void forward()
{
  digitalWrite(2, HIGH);
  digitalWrite(4, LOW);
  digitalWrite(5, HIGH);
  digitalWrite(7, LOW);
}

void backward()
{
  digitalWrite(2, LOW);
  digitalWrite(4, HIGH);
  digitalWrite(5, LOW);
  digitalWrite(7, HIGH);
}


RF24 radio(9, 10);

uint64_t addresses[2] = {0xF0F0F0F0E1LL, 0xF0F0F0F0D2LL}; // адреса для приема и передачи данных. используем addresses[0] при посылке, addresses[1] при отправке ответа

long int data[2];

void setup() {
    pinMode(2, OUTPUT);
    pinMode(3, OUTPUT);
    pinMode(4, OUTPUT);
    pinMode(5, OUTPUT);
    pinMode(6, OUTPUT);
    pinMode(7, OUTPUT);

    radio.begin();                                        // Инициируем работу nRF24L01+
    radio.setChannel      (125);                          // Указываем канал передачи данных (от 0 до 127), 5 - значит передача данных осуществляется на частоте 2,405 ГГц (на одном канале может быть только 1 приёмник и до 6 передатчиков)
    radio.setDataRate     (RF24_1MBPS);                   // Указываем скорость передачи данных (RF24_250KBPS, RF24_1MBPS, RF24_2MBPS), RF24_1MBPS - 1Мбит/сек
    radio.setPALevel      (RF24_PA_HIGH);                 // Указываем мощность передатчика (RF24_PA_MIN=-18dBm, RF24_PA_LOW=-12dBm, RF24_PA_HIGH=-6dBm, RF24_PA_MAX=0dBm)
    radio.setAutoAck      (1);
    radio.enableAckPayload();
    radio.setPayloadSize  (sizeof(data));
    radio.openWritingPipe (addresses[1]);                 // канал для передачи данных
    radio.openReadingPipe (1,addresses[0]);               // канал для приема данных
    radio.startListening  ();                             // Включаем приемник  

    Serial.begin(9600);
    Serial.println("hello");  
}

void loop() {
    if(radio.available())
    {
        radio.read(&data, sizeof(data));
        
        // готовим данные для отправки
        long int t = (long int)(millis() / 1000);
        // передаем подготовленные данные отправителю
        radio.writeAckPayload(1, &t, sizeof(t));

        int val1;
        int val2;

        if (data[0] > 530)
        {
            forward();
            val1 = 100 + (data[0] - 512) * 150  / 512;
        }
        else if (data[0] < 510)
        {
            backward();
            val1 = 100 + (512 - data[0]) * 150 / 512;
        }
        else
        {
            backward();
            val1 = 0;
        }

        if (data[1] > 530)
        {
            val2 = (data[1] - 512) * 150  / 512;
        }
        else if (data[1] < 510)
        {
            val2 = - (512 - data[1]) * 150 / 512;
        }
        else
        {
            val2 = 0;
        }        

        int l = max(0, min(val1 - val2, 255));
        int r = max(0, min(val1 + val2, 255));
        
        analogWrite(3, l);
        analogWrite(6, r);
        
        Serial.print("X: "); Serial.println(data[0]);        
        Serial.print("Y: "); Serial.println(data[1]);
        Serial.print("val1: "); Serial.println(val1);
        Serial.print("val2: "); Serial.println(val2);
        Serial.print("l: "); Serial.println(l);
        Serial.print("r: "); Serial.println(r);

        //delay(1000);     
    }
}
