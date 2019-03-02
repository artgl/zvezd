#include <Wire.h>
#include <MPU6050.h>
#include <Servo.h>

MPU6050 mpu;
Servo servo1; 

void setup() 
{
pinMode(3, INPUT);


  pinMode(10, OUTPUT);
  pinMode(11, INPUT);
  pinMode(6, OUTPUT);
  pinMode(7, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);
  servo1.attach(5);
  servo1.write(15); 
  
  Serial.begin(115200);

  Serial.println("Initialize MPU6050");

  while(!mpu.begin(MPU6050_SCALE_2000DPS, MPU6050_RANGE_2G))
  {
    Serial.println("Could not find a valid MPU6050 sensor, check wiring!");
    delay(500);
  }

  // If you want, you can set accelerometer offsets
  // mpu.setAccelOffsetX();
  // mpu.setAccelOffsetY();
  // mpu.setAccelOffsetZ();
  
  checkSettings();
}

void checkSettings()
{
  Serial.println();
  
  Serial.print(" * Sleep Mode:            ");
  Serial.println(mpu.getSleepEnabled() ? "Enabled" : "Disabled");
  
  Serial.print(" * Clock Source:          ");
  switch(mpu.getClockSource())
  {
    case MPU6050_CLOCK_KEEP_RESET:     Serial.println("Stops the clock and keeps the timing generator in reset"); break;
    case MPU6050_CLOCK_EXTERNAL_19MHZ: Serial.println("PLL with external 19.2MHz reference"); break;
    case MPU6050_CLOCK_EXTERNAL_32KHZ: Serial.println("PLL with external 32.768kHz reference"); break;
    case MPU6050_CLOCK_PLL_ZGYRO:      Serial.println("PLL with Z axis gyroscope reference"); break;
    case MPU6050_CLOCK_PLL_YGYRO:      Serial.println("PLL with Y axis gyroscope reference"); break;
    case MPU6050_CLOCK_PLL_XGYRO:      Serial.println("PLL with X axis gyroscope reference"); break;
    case MPU6050_CLOCK_INTERNAL_8MHZ:  Serial.println("Internal 8MHz oscillator"); break;
  }
  
  Serial.print(" * Accelerometer:         ");
  switch(mpu.getRange())
  {
    case MPU6050_RANGE_16G:            Serial.println("+/- 16 g"); break;
    case MPU6050_RANGE_8G:             Serial.println("+/- 8 g"); break;
    case MPU6050_RANGE_4G:             Serial.println("+/- 4 g"); break;
    case MPU6050_RANGE_2G:             Serial.println("+/- 2 g"); break;
  }  

  Serial.print(" * Accelerometer offsets: ");
  Serial.print(mpu.getAccelOffsetX());
  Serial.print(" / ");
  Serial.print(mpu.getAccelOffsetY());
  Serial.print(" / ");
  Serial.println(mpu.getAccelOffsetZ());
  
  Serial.println();
}

int vverx()
{
  int good_result = 0; 
  for (int p=0; p<5; p=p+1)
  {
    Vector  rawAccel = mpu.readRawAccel();

    if (rawAccel.XAxis > 6000)
    {
     good_result=good_result+1;
     }
     delay(40);
  }

  Serial.println(good_result);

  if (good_result == 5)
    return 1;

  return 0;
}



int naklon_protiv_chsovoi ()
{

   const int c = 3;
   int good_result = 0; 
  for (int p=0; p<c; p=p+1)
  {
    Vector  rawAccel = mpu.readRawAccel();

    if (rawAccel.XAxis < -3800)
    {
     good_result=good_result+1;
     }
     delay(10);
  }

  Serial.println(good_result);

  if (good_result == c)
    return 1;

  return 0;
  

  
}

long yltrozvyk()
{

int trigPin = 10;    //Триггер – зеленый проводник

int echoPin = 11;    //Эхо – желтый проводник

long duration, cm, inches;


// Датчик срабатывает и генерирует импульсы шириной 10 мкс или больше

// Генерируем короткий LOW импульс, чтобы обеспечить «чистый» импульс HIGH:

digitalWrite(trigPin, LOW);

delayMicroseconds(5);

digitalWrite(trigPin, HIGH);

delayMicroseconds(10);

digitalWrite(trigPin, LOW);

// Считываем данные с ультразвукового датчика: значение HIGH, которое

// зависит от длительности (в микросекундах) между отправкой

// акустической волны и ее обратном приеме на эхолокаторе.

pinMode(echoPin, INPUT);

duration = pulseIn(echoPin, HIGH);

// преобразование времени в расстояние

cm = (duration/2) / 29.1;

return cm;


inches = (duration/2) / 74;

Serial.print(inches);


Serial.print(cm);

Serial.print("cm");

Serial.println();

delay(250);

}



 int vniz()
{
  int good_result = 0; 
  for (int p=0; p<5; p=p+1)
  {
    Vector  rawAccel = mpu.readRawAccel();

    if (rawAccel.XAxis < 6000)
    {
     good_result=good_result+1;
     }

     delay(40);
  }

  if (good_result == 5)
    return 1;

  return 0;
}




int i = 0;

void loop()
{
 


  if (yltrozvyk() > 100)
  {
     delay(1000000);
  }
  
  digitalWrite(6, HIGH);
  digitalWrite(7, HIGH);
  digitalWrite(8, HIGH);
  digitalWrite(9, HIGH);


  Vector rawAccel = mpu.readRawAccel();
  
 

  while (vverx() == 0)
  {
     // do nothing
     
  Vector rawAccel = mpu.readRawAccel();
      Serial.println(rawAccel.XAxis);
  }

  
  
  Serial.println("vverh");/////////////
  servo1.write(110);
  

  while (naklon_protiv_chsovoi() == 0)
  {
    
  Vector rawAccel = mpu.readRawAccel();
     Serial.println(rawAccel.XAxis);
     // do nothing
  }

  
       digitalWrite(6, LOW);
      digitalWrite(7, LOW);
      digitalWrite(8, LOW);
      digitalWrite(9, LOW);
      
  


/*

 naklon protiv chfcovoi  <1200~600>  naklon po chfcovoi
 
*/    



  
  
  servo1.write(0); 
  Serial.println("vniz"); //////////////
  
  
 
   delay(2000);


  i = i + 1;     
  Serial.println(i);
  
}
