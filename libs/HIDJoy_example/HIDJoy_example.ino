// *******************************
// USBtx by Rickey Ward
//
// Gamepad with Left and Right
// analog axis - converterd from 
// spektrum flight transmitter
//
// Ex version with calibration mode
//
// ******************************

//include VUSB Library
#include <HIDJoy.h>

// !!!! скопировать WInterrupts.c из HIDJoy в Arduino->hardware->avr->cores->arduino
// green usb - D2
// white usb - D7

//Create instance of HIDJoystick
HIDJoy joy;

void setup() {
  //start USB communication
  joy.begin();
}

int data = 0;
int add = 1;

void loop()
{
    //do usb stuff, important to be called often.
    joy.poll();

    //grab data, send it to usb

    data = data + add;
    if (data == 255)
        add = -1;
    if (data == 0)
        add = 1;

    delay(1);
     
    uint8_t lx = (uint8_t)data;
    uint8_t ly = (uint8_t)data;
    uint8_t rx = (uint8_t)data;
    uint8_t ry = (uint8_t)data;
    
    joy.writeGame(lx,ly,rx,ry);
      
  
}//end loop

