/*
 * IRremote: IRrecvDemo - demonstrates receiving IR codes with IRrecv
 * An IR detector/demodulator must be connected to the input RECV_PIN.
 * Version 0.1 July, 2009
 * Copyright 2009 Ken Shirriff
 * http://arcfn.com
 */

#include <IRremote.h>

#include <controller.h>

/* =============================================================== */

int RECV_PIN = 11;
IRrecv irrecv(RECV_PIN);

/* =============================================================== */

void setup()
{
  Serial.begin(9600);
  irrecv.enableIRIn(); // Start the receiver
}

void loop()
{
    decode_results results;
    if (irrecv.decode(&results))
    {
        ControllerRes res;
        if (-1 != controller_decode(results, res))
        {
            Serial.print("throttle: ");
            Serial.println(res.throttle);
            Serial.print("left-right: ");
            Serial.println(res.leftright);
            Serial.print("up-down: ");
            Serial.println(res.updown);
            Serial.print("left: ");
            Serial.println(res.left);
            Serial.print("right: ");
            Serial.println(res.right);
            Serial.print("photo: ");
            Serial.println(res.photo);
            Serial.print("light: ");
            Serial.println(res.light);
            Serial.print("video: ");
            Serial.println(res.video);
            Serial.print("b1: ");
            Serial.println(res.b1);
            Serial.print("b2: ");
            Serial.println(res.b2);
        }
        irrecv.resume();
    }
    delay(1000);
}
