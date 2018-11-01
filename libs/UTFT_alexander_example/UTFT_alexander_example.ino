// UTFT_Demo_160x128_Serial (C)2012 Henning Karlsen
// web: http://www.henningkarlsen.com/electronics
//
// This program is a demo of how to use most of the functions
// of the library with a supported display modules.
//
// This demo was made for modules with a screen resolution 
// of 160x128 pixels.
//
// This program requires the UTFT library.
//

#include <UTFT.h>

// Declare which fonts we will be using

// UTFT _NAME_ (model, SDA, CLK, CS, RST, RS) 
UTFT myGLCD(ST7735,A2,A1,A5,A4,A3);


extern uint8_t SmallFont[];
void setup() {
  myGLCD.InitLCD(1);
  myGLCD.clrScr();
  myGLCD.setFont(SmallFont);
  myGLCD.print("Hello, world!", CENTER, 0);  
  delay(1000);
  
  
  }

void loop() {

}
