#include <Wire.h>
#include "cactus_io_BME280_I2C.h"
// Create BME280 object
// BME280_I2C bme; // I2C using address 0x77
 BME280_I2C bme(0x76); // I2C using address 0x76
 const int analogInPin = A3; // Указываем пин, к которому подключен датчик
int sensorValue = 0; // Объявляем переменную для хранения значений с датчика 

void setup() {

Serial.begin(9600);


if (!bme.begin()) {
Serial.println("Could not find a valid BME280 sensor, check wiring!");
while (1);
}

bme.setTempCal(-1);// Temp was reading high so subtract 1 degree

}

void loop() {
sensorValue = analogRead(analogInPin); //считываем значения с датчика
bme.readSensor();

Serial.print("загрязнение  "); Serial.println(sensorValue);

Serial.print("давление  "); Serial.println(bme.getPressure_MB());

Serial.print("влажность  "); Serial.println(bme.getHumidity()); 

Serial.print("температура  "); Serial.println(bme.getTemperature_C()); 

Serial.println(" ");

delay(2000); //just here to slow down the output.
} 
