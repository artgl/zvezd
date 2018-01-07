#include <SPI.h>                                          // Подключаем библиотеку  для работы с шиной SPI
#include <nRF24L01.h>                                     // Подключаем файл настроек из библиотеки RF24
#include <RF24.h>                                         // Подключаем библиотеку  для работы с nRF24L01+

RF24 radio(9, 10);                                        // Создаём объект radio   для работы с библиотекой RF24, указывая номера выводов nRF24L01+ (CE, CSN)

uint64_t addresses[2] = {0xF0F0F0F0E1LL, 0xF0F0F0F0D2LL}; // адреса для приема и передачи данных. используем addresses[0] в передатчике, addresses[1] в приемнике

long int data[2];                                         // Создаём массив для приёма/передачи данных

void setup(){
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

void loop(){
    if(radio.available()){                                // Если в буфере имеются принятые данные
        radio.read(&data, sizeof(data));                  // Читаем данные в массив data и указываем сколько байт читать

        // готовим данные для отправки
        long int t = (long int)(millis() / 1000);
        // передаем подготовленные данные отправителю
        radio.writeAckPayload(1, &t, sizeof(t));     

        Serial.println(data[0]);        
        Serial.println(data[1]);
        delay(100);
    }
}

