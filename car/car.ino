#include "SoftwareSerial.h"
#include "Servo.h"

int lw_1 = 2; 
int lw_2 = 3;
int rw_1 = 4;
int rw_2 = 5;

int ls = A0;
int rs = A1;

int trigPin = 8;
int echoPin = 9; 

const int min_dist = 15; //cm

int going_forward = 1;

const int time_1cm = 30; // время мс чтобы проехать 1 см  

int step_delay = 100;


SoftwareSerial myserial(10, 11); // RX, TX

Servo myservo;


void forward(int ms, int delay1)
{
  digitalWrite(lw_1, LOW); digitalWrite(rw_1, LOW); digitalWrite(lw_2, HIGH); digitalWrite(rw_2, HIGH);
  delay(ms);
  digitalWrite(lw_2, LOW); digitalWrite(rw_2, LOW);
  delay(delay1);

}

void backward(int ms, int delay1)
{
  digitalWrite(lw_1, HIGH); digitalWrite(rw_1, HIGH); digitalWrite(lw_2, LOW); digitalWrite(rw_2, LOW);
  delay(ms);
  digitalWrite(lw_1, LOW); digitalWrite(rw_1, LOW);  
  delay(delay1);
}

void right(int ms, int delay1)
{
  digitalWrite(lw_1, HIGH); digitalWrite(rw_1, LOW); digitalWrite(lw_2, LOW); digitalWrite(rw_2, HIGH);
  delay(ms);
  digitalWrite(lw_1, LOW); digitalWrite(rw_2, LOW);  
  delay(delay1);
}

void left(int ms, int delay1)
{
  digitalWrite(lw_1, LOW); digitalWrite(rw_1, HIGH); digitalWrite(lw_2, HIGH); digitalWrite(rw_2, LOW);
  delay(ms);
  digitalWrite(lw_2, LOW); digitalWrite(rw_1, LOW);  
  delay(delay1);
}


int is_black(int val)
{
  if (val < 350)
    return 1;
  return 0;
}

int is_white(int val)
{
  return 1 - is_black(val);
}

int distance()
{
  unsigned long duration;
  int cm = 3000;

  while (cm >= 3000)
  {
      digitalWrite(trigPin, LOW); 
      delayMicroseconds(2); 
      digitalWrite(trigPin, HIGH); 
      delayMicroseconds(10);
      digitalWrite(trigPin, LOW);
      duration = pulseIn(echoPin, HIGH); 
      cm = duration / 58;
      delay(50);
  }
  return cm; 
}

void myservo0()
{
    myservo.attach(13);
    myservo.write(0);
    delay(300);
    myservo.detach();
}

void myservo90()
{
    myservo.attach(13);
    myservo.write(80);
    delay(300);
    myservo.detach();
}

void setup() { 
  pinMode(lw_1, OUTPUT); 
  pinMode(lw_2, OUTPUT); 
  pinMode(rw_1, OUTPUT); 
  pinMode(rw_2, OUTPUT);
  pinMode(13, OUTPUT);

  pinMode(trigPin, OUTPUT); 
  pinMode(echoPin, INPUT); 

  myserial.begin(9600);
  myserial.println("Car is ready");
  Serial.begin(9600);

  myservo90();
  
  delay(3000);

  //устанавливаем задержкуна каждом шагу в зависимости от показаний радара
  digitalWrite(13, HIGH);
  delay(50);
  step_delay = distance() * 2;
  digitalWrite(13, LOW);  
  Serial.println(step_delay);
  delay(5000);
}

void loop()
{  
    int dist = distance();
    int lsv = analogRead(ls);
    int rsv = analogRead(rs);
    
    if (going_forward == 1)
    {        
        if (dist > min_dist)
        {
            if (is_black(rsv))
            {
                forward(35, step_delay);
            }
            else // правый датчик съехал с линии
            {
                if (is_black(lsv))
                {
                    left(20, step_delay / 2);
                    while (is_white(analogRead(rs)))
                    {
                        left(20, step_delay / 2);
                    }
                }
                else
                {
                    right(20, step_delay / 2);
                }
            }
        }
        else //впервые увидели препятствие
        {
            going_forward = 0;
          
            // отъезжаем назад если препятствие оказалось слишком близко

            int back_time = (min_dist - dist - 3) * time_1cm;
            if (back_time > 40)
            {
                backward(back_time, step_delay);
            }          

            // поворачиваем радар на 90 градусов вправо и разворачиваемся влево пока снова
            // не увидим препятствие

            myservo0();
            while (distance() > int(min_dist * 1.7))
            {
                left(20, step_delay / 2);
            }

            // нужно съехать с линии. Объезд будет закончен, когда мы снова окажемся на линии
            while (is_black(analogRead(ls)) || is_black(analogRead(rs)))
            {
                forward(35, step_delay);
            }
        }

    }
    else //продолжаем объезжать препятствие
    {
        if (is_black(lsv) || is_black(rsv))
        {
            // один из сенсоров показывает что мы на линии. Объезд закончен.
            going_forward = 1;
            myservo90();          
        }
        else
        {
            if (dist > int(min_dist * 1.7))
            {
                right(20, step_delay / 2);
            }
            else
            {
                left(40, step_delay / 2); //слегка отворачиваем влево чтобы увеличить радиус поворота
                forward(35, step_delay);
                forward(35, step_delay);
            }
        }
    }

//    myserial.print(lsv);
//    myserial.print(" ");
//    myserial.println(rsv);    
//    myserial.print(" ");
//    myserial.print(going_forward);    
//    myserial.print(" ");
//    myserial.print(dist);    
//    myserial.println("");
}




