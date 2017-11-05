//#include <ServoTimer2.h>
#include <Servo.h>
#include <SoftwareSerial.h>


//ServoTimer2 myservo;  // create servo object to control a servo
Servo myservo;  // create servo object to control a servo

SoftwareSerial mySerial(10, 11); // RX, TX

int echoPin = 6; 
int trigPin = 5; 
 
void setup() { 

//  Serial.begin (9600); 
  mySerial.begin (9600); 
  pinMode(trigPin, OUTPUT); 
  pinMode(echoPin, INPUT); 
  myservo.attach(9);
  myservo.write(90);
  delay(2000);

} 

double avg = 0;


int distance()
{
  int duration, cm; 
  digitalWrite(trigPin, LOW); 
  delayMicroseconds(2); 
  digitalWrite(trigPin, HIGH); 
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH); 
  cm = duration / 58;
  
  delay(50);
  return cm; 
}



 
void loop() { 

  int i;
  for (i = 0; i < 180; i++)
  {

    myservo.write(i);
    
    delay(100);

    int cm = distance(); 
    if (cm > 0)
      avg = avg * 0.9 + 0.1 * cm;
  
    mySerial.print(i); 
    mySerial.print(" "); 
    mySerial.println((int)cm); 

  };
  
  for (i = 180; i > 0; i--)
  {

    myservo.write(i);
    
    delay(100);

    int cm = distance(); 
    if (cm > 0)
      avg = avg * 0.9 + 0.1 * cm;
  
    mySerial.print(i); 
    mySerial.print(" "); 
    mySerial.println((int)cm); 

  }  
 
}
