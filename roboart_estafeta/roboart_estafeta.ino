#include <Servo.h>
 
Servo  s1;
 
const int speed_delay = 0;
 
int readTouch(int pin)
{
 
  int c = 0;
  for (int i = 0; i < 5; i++)
  {
    int z = digitalRead(pin);
    Serial.print("z");
    Serial.println(z);
    if (z == 1)
      c = c + 1;
  }
 
  if (c == 5)
    return 1;
  return 0;
}
 
 
void setup()
{
  pinMode(12,INPUT);
  pinMode(6,INPUT);
  pinMode(7,INPUT);
  pinMode(3,OUTPUT);
  pinMode(2,OUTPUT);
  pinMode(5,OUTPUT);
  pinMode(4,OUTPUT);
  Serial.begin(9600);
  s1.attach(11);
  s1.write(80);
  Serial.println("fhdfhisfhf");
  while (digitalRead(12) == 1)
  {
    Serial.println("Waiting");
  }
}
 
 
void ahead()
  {
   digitalWrite(3,HIGH);
   digitalWrite(2,LOW);
   digitalWrite(5,HIGH);
   digitalWrite(4,LOW);
   delay(40);
   off();
  }
 
 
void right()
{
   digitalWrite(3,LOW);
   digitalWrite(2,HIGH);
   digitalWrite(5,HIGH);
   digitalWrite(4,LOW);
   delay(40);
   off();
}
 
void left()
{
   digitalWrite(3,HIGH);
   digitalWrite(2,LOW);
   digitalWrite(5,LOW);
   digitalWrite(4,HIGH);
   delay(40);
   off();
}
void off()
{
   digitalWrite(3,LOW);
   digitalWrite(2,LOW);
   digitalWrite(5,LOW);
   digitalWrite(4,LOW);
   delay(speed_delay);
 
}
 //____________________________________________________________________________________________________________________________________________
void stikovka_napravo()
{
   digitalWrite(3,LOW);
   digitalWrite(2,HIGH);
   digitalWrite(5,LOW);
   digitalWrite(4,LOW);
   delay(40);
   
}
 
void stikovka_nalevo()
{
   digitalWrite(3,LOW);
   digitalWrite(2,LOW);
   digitalWrite(5,LOW);
   digitalWrite(4,HIGH);
   delay(40);
   
}
 

 //____________________________________________________________________________________________________________________________________________
void loop()
{
      int rightsensor_parking = readTouch(7);
      int leftsensor_parking = readTouch(6);
      int rightsensor = analogRead(A7);
      int leftsensor = analogRead(A6);
  while (rightsensor_parking == 1 && leftsensor_parking == 1)
  {   
    
    if (rightsensor >= 600 && leftsensor < 600) //едем прямо
    {
      Serial.println("ahead");
       ahead();
    }
   
    if (rightsensor < 600 && leftsensor >= 600) //поворачиваем налево
    {
       Serial.println("left");
      left();
    }
   
    if (rightsensor < 600 && leftsensor < 600) //поворачиваем направо
    {
       Serial.println("right");
      right();
    }
     
    if (rightsensor >= 600 && leftsensor >= 600) //поворачиваем налево
    {
       Serial.println("left");
      left();
    }

    rightsensor_parking = readTouch(7);
    leftsensor_parking = readTouch(6);
    rightsensor = analogRead(A7);
    leftsensor = analogRead(A6);   
  }
         
  if (rightsensor_parking == 1 && leftsensor_parking == 0) //стыкуемся, поворачивая налево
  {
    Serial.println("parking_left");
    stikovka_nalevo();
  }
 
  if (rightsensor_parking == 0 && leftsensor_parking == 1) //стыкуемся, поворачиваясь направо
  {
    Serial.println("parking_right");
    stikovka_napravo();
  }
  if (rightsensor_parking == 0 && leftsensor_parking == 0)  //смэрть
  {
    Serial.println("dead");
    off();
    s1.write(0);
    delay(1000);
    s1.write(80);
    delay(49674582);
  }
 }
