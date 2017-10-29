// Тестировалось на Arduino IDE 1.0.1
#include <AFMotor.h>  // Подключаем библиотеку для работы с шилдом 
#include <Servo.h>  // Подключаем библиотеку для работы с сервоприводами, можно не подключать

// Подключаем моторы к клеммникам M1, M2, M3, M4
AF_DCMotor motor1(1);
AF_DCMotor motor2(2);
AF_DCMotor motor3(3);
AF_DCMotor motor4(4);

void setup() {
  // Задаем максимальную скорость вращения моторов (аналог работы PWM) 
  motor1.setSpeed(255);
  motor1.run(RELEASE);
  motor2.setSpeed(255);
  motor2.run(RELEASE);
  motor3.setSpeed(255);
  motor3.run(RELEASE);
  motor4.setSpeed(255);
  motor4.run(RELEASE);
}

int i;

void loop() {
  // Двигаемся условно вперед одну секунду 
  motor1.run(FORWARD); // Задаем движение вперед
  motor2.run(FORWARD);
  motor3.run(FORWARD);
  motor4.run(FORWARD);
  motor1.setSpeed(255); // Задаем скорость движения
  motor2.setSpeed(255); 
  motor3.setSpeed(255); 
  motor4.setSpeed(255); 
  delay(1000);
  
  // Останавливаем двигатели
  /* Очень не рекомендуем резко переключать направление вращения двигателей.
  Лучше дать небольшой промежуток времени.*/
  
  motor1.run(RELEASE); 
  motor2.run(RELEASE);
  motor3.run(RELEASE);
  motor4.run(RELEASE);
  delay(500);
  
  // Двигаемся в обратном направлении
  motor1.run(BACKWARD);  // Задаем движение назад
  motor2.run(BACKWARD);
  motor3.run(BACKWARD);
  motor4.run(BACKWARD);
  motor1.setSpeed(255);  // Задаем скорость движения 
  motor2.setSpeed(255); 
  motor3.setSpeed(255); 
  motor4.setSpeed(255); 
  delay(1000);
  
  // Останавливаем двигатели  
  motor1.run(RELEASE);
  motor2.run(RELEASE);
  motor3.run(RELEASE);
  motor4.run(RELEASE);
  delay(500);
  
  // Разгоняем двигатели в одном направлении
  motor1.run(FORWARD);
  motor2.run(FORWARD);
  motor3.run(FORWARD);
  motor4.run(FORWARD);
  for (i=0; i<255; i++) {
    motor1.setSpeed(i); 
    motor2.setSpeed(i); 
    motor3.setSpeed(i); 
    motor4.setSpeed(i); 
    delay(10);
 }
 
 // Останавливаем двигатели  
  motor1.run(RELEASE);
  motor2.run(RELEASE);
  motor3.run(RELEASE);
  motor4.run(RELEASE);
  delay(500);
  
  // Разгоняем двигатели в обратном направлении
  motor1.run(BACKWARD);
  motor2.run(BACKWARD);
  motor3.run(BACKWARD);
  motor4.run(BACKWARD);
  for (i=255; i>=0; i--) {
    motor1.setSpeed(i); 
    motor2.setSpeed(i); 
    motor3.setSpeed(i); 
    motor4.setSpeed(i); 
    delay(10);
 }
  // Останавливаем движение  
  motor1.run(RELEASE);
  motor2.run(RELEASE);
  motor3.run(RELEASE);
  motor4.run(RELEASE);
  delay(500);
}



