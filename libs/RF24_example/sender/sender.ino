#include <SPI.h>                                          // Подключаем библиотеку для работы с шиной SPI
#include <nRF24L01.h>                                     // Подключаем файл настроек из библиотеки RF24
#include <RF24.h>                                         // Подключаем библиотеку для работы с nRF24L01+

RF24 radio(9, 10);                                        // Создаём объект radio для работы с библиотекой RF24, указывая номера выводов nRF24L01+ (CE, CSN)

uint64_t addresses[2] = {0xF0F0F0F0E1LL, 0xF0F0F0F0D2LL}; // адреса для приема и передачи данных. используем addresses[0] в передатчике, addresses[1] в приемнике

long int  data[2];                                        // Создаём массив для приёма/передачи данных

void setup(){
    radio.begin();                                        // Инициируем работу nRF24L01+
    radio.setChannel      (125);                          // Указываем канал передачи данных (от 0 до 127), 5 - значит передача данных осуществляется на частоте 2,405 ГГц (на одном канале может быть только 1 приёмник и до 6 передатчиков)
    radio.setDataRate     (RF24_1MBPS);                   // Указываем скорость передачи данных (RF24_250KBPS, RF24_1MBPS, RF24_2MBPS), RF24_1MBPS - 1Мбит/сек
    radio.setPALevel      (RF24_PA_HIGH);                 // Указываем мощность передатчика (RF24_PA_MIN=-18dBm, RF24_PA_LOW=-12dBm, RF24_PA_HIGH=-6dBm, RF24_PA_MAX=0dBm)
    radio.setAutoAck      (1);
    radio.enableAckPayload();
    radio.setPayloadSize  (sizeof(data));
    radio.openWritingPipe (addresses[0]);                 // канал для передачи данных
    radio.openReadingPipe (1, addresses[1]);              // канал для приема данных

    Serial.begin(9600);
    Serial.println("hello");
}

void loop(){
    data[0] = analogRead(A0);                             // считываем показания Trema слайдера с вывода A1 и записываем их в 0 элемент массива data
    data[1] = analogRead(A1);                             // считываем показания Trema потенциометра с вывода A2 и записываем их в 1 элемент массива data
    
    radio.powerUp();
    delay(1);

    int res = radio.write(&data, sizeof(data));

    radio.powerDown();

    if (res)
    {
        Serial.println("ok");
        if (radio.isAckPayloadAvailable())
        {
            long int t;
            radio.read(&t, sizeof(t));
            Serial.print("Response: "); Serial.println(t);
        }
    }
    else
    {
        Serial.println("err");
    }
    delay(50);
}

