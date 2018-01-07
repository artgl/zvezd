#include <Adafruit_GFX.h>
#include <Adafruit_PCD8544.h>
Adafruit_PCD8544 display = Adafruit_PCD8544(3, 4, 5, 6, 7);

void setup() {
    // инициализация и очистка дисплея
    display.begin();
    display.clearDisplay();
    display.display();
    
    display.setContrast(50); // установка контраста
    delay(1000);
    display.setTextSize(1);  // установка размера шрифта
    display.setTextColor(BLACK); // установка цвета текста
    display.setCursor(0,0); // установка позиции курсора
  
    display.println("Hello, world!");
    display.display();

    display.drawCircle(20, 20, 5, BLACK);
    display.drawRect(10, 10, 20, 20, BLACK);    
    display.drawCircle(60, 20, 5, BLACK);
    display.drawRect(50, 10, 20, 20, BLACK);    
    display.drawRect(5, 40, 70, 5, BLACK);    
    display.display();    
}

void loop() {
}

