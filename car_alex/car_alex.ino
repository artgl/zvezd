#include "Servo.h"
unsigned long i_got;  
unsigned long alalalalala;  
unsigned long balalalalala;  
unsigned long abalalalalala;  
unsigned long krytilka;

Servo myservo;


void setup()
{
pinMode(43,INPUT);
pinMode(41,INPUT);
pinMode(45,INPUT);
pinMode(47,INPUT);
pinMode(49,INPUT);


pinMode(3,OUTPUT);
pinMode(4,OUTPUT);
pinMode(5,OUTPUT);
pinMode(6,OUTPUT);
pinMode(7,OUTPUT);
pinMode(12,INPUT);
pinMode(13,INPUT);





myservo.attach(46);

Serial.begin(9600);
}
void loop()
{
  int i;
  int j;
  int k;
  
  alalalalala=pulseIn(41,HIGH); //  pravyi joystick levo-pravo
  balalalalala=pulseIn(45,HIGH); // pravaya krytilka
  krytilka=pulseIn(43,HIGH);  // swa
  
  // 47 - levyi joystick levo-pravo
  
  i_got=pulseIn(53,HIGH);  // levyi joystick vverh-niz
  abalalalalala=pulseIn(49,HIGH);   // pravyi joystick vverh-niz

  if (alalalalala < 1450)
  {
     k = -50 + (int)((alalalalala - 1000) / 10 );
     Serial.println("< 1450");
  }
  else if (alalalalala > 1550)
  {
     k = 50 - (int)((2000 - alalalalala) / 10);
     Serial.println(" > 1550");
  }
  else
  {
     k = 0;
  }

  if(abalalalalala>1550)
  {
    i = (abalalalalala-1500)/5 + 150 - k * 4 ;
    j = (abalalalalala-1500)/5 + 150 + k * 4 ;
    if (i > 255) i = 255;
    if (j > 255) j = 255;        
    if (i < 0)   i = 0;
    if (j < 0)   j = 0;        
    analogWrite(2,i);
    analogWrite(7,j); 
    digitalWrite(3,HIGH);
    digitalWrite(4,LOW);
    digitalWrite(5,HIGH);
    digitalWrite(6,LOW);
  }

if(abalalalalala<1550 && abalalalalala>1450)
{
    //левый дж лв-пр
  analogWrite(2,0);
  analogWrite(7,0);   
}


if(abalalalalala<1450 && abalalalalala>0)
{
   //левый дж лв-пр
  
   i= (-1) * (abalalalalala-1500)/5+150 - k * 4;  
   j= (-1) * (abalalalalala-1500)/5+150 + k * 4;  
    if (i > 255) i = 255;
    if (j > 255) j = 255;        
    if (i < 0)   i = 0;
    if (j < 0)   j = 0;        
  analogWrite(2,i);
  analogWrite(7,j);  
  digitalWrite(3,LOW);
  digitalWrite(4,HIGH);
  digitalWrite(5,LOW);
  digitalWrite(6,HIGH);
  
   
}

if(alalalalala>1800 && abalalalalala > 1450 && abalalalalala < 1550)
{
   analogWrite(2,255);
  analogWrite(7,255); 
 digitalWrite(3,LOW);
 digitalWrite(4,HIGH);
 digitalWrite(5,HIGH);
 digitalWrite(6,LOW);    
}

if (alalalalala<1200 && alalalalala > 0 && abalalalalala > 1450 && abalalalalala < 1550)
{
  analogWrite(2,255);
  analogWrite(7,255);  
  digitalWrite(3,HIGH);
  digitalWrite(4,LOW);
  digitalWrite(5,LOW);
  digitalWrite(6,HIGH);  
 
}
 
 
   if(pulseIn(43,HIGH) > 1900)
  {
    myservo.write(90);
   
  } 
   else
  {
    myservo.write(0);

  }
 
 
 
 
 Serial.println(k);


// Serial.println(krytilka);
 Serial.println(i);
 Serial.println(j);
// Serial.print("alalalalala ");   //левый дж лв-пр
// Serial.println(alalalalala);
// Serial.print("balalalalala "); //правый дж лв-пр
// Serial.println(balalalalala);
// Serial.print("abalalalalala "); //левый дж вх-вн
// Serial.println(abalalalalala);
// Serial.print("i_got ");//газ
// Serial.println(i_got);
     














}







