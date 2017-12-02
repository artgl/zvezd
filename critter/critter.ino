#include "Servo.h"
#include <IRremote.h>
#include <controller.h>

/* =============================================================== */

int RECV_PIN = 11;
IRrecv irrecv(RECV_PIN);

Servo ser1;
Servo ser2;
Servo ser3;
Servo ser4;

void setup() {
  Serial.begin(9600);
 
  irrecv.enableIRIn();

  ser1.write(90);
  ser2.write(90);
  ser3.write(90);
  ser4.write(90);

  ser1.attach(4);
  ser2.attach(5);
  ser3.attach(6);
  ser4.attach(7);

  Serial.println("Hello");
  
}

void servo_move_to(Servo *ser, int grad, int step_delay)
{
    int prev_grad = ser->read();
    int i;
    if (grad > prev_grad)
    {
        for (i = prev_grad; i <= grad; i++)
        {
            ser->write(i);
            delay(step_delay);
        }
    }
    else
    {
        for (i = prev_grad; i >= grad; i--)
        {
            ser->write(i);
            delay(step_delay);
        }
    }  
}

const char *forward  = "a030c150b150d030a150c030b030d150a120c060b090d090";
const char *backward = "a150c030b150d030a030c150b030d150a120c060b090d090";
const char *right = "a030b150a150b030a120c060b090d090";
const char *left  = "c150d030c030d150a120c060b090d090";
const char *no = "a020b010a040a020a120c060b090d090";
const char *yes = "a030b010b090b010a120c060b090d090";

int pos = 0;
const char *cmd = 0;
const char *new_cmd = 0;
int has_new_command = 0;

void loop() {
    // put your main code here, to run repeatedly:
  
    decode_results results;
    if (irrecv.decode(&results))
    {
        ControllerRes res;
        if (-1 != controller_decode(results, res))
        {
            new_cmd = 0;
            has_new_command = 1;

            if (res.left)
            {
                new_cmd = left;
            }
            else if (res.right)
            {
                new_cmd = right;
            }
            else if (res.photo)
            {
                new_cmd = forward;
            }
            else if (res.light)
            {
                new_cmd = backward;
            }
            else if (res.b1)
            {
                new_cmd = yes;
            }
            else if (res.b2)
            {
                new_cmd = no;
            }
        }
        irrecv.resume();       
    }

    if (pos == 0)
    {
        if (has_new_command)
            cmd = new_cmd;
        else
            cmd = 0;
        has_new_command = 0;
    }
        
    if (cmd == 0)
        return;
  
    int b1 = cmd[pos + 0];
    int b2 = cmd[pos + 1];
    int b3 = cmd[pos + 2];
    int b4 = cmd[pos + 3];
  
    int grad = (b2 - '0') * 100 + (b3 - '0') * 10 + (b4 - '0');
  
    Serial.println((char) b1);
    Serial.println(grad);
  
    if (b1 == 'a')
    {
      servo_move_to(&ser1, grad, 5);
    }
    if (b1 == 'b')
    {
      servo_move_to(&ser2, grad, 5);
    }
    if (b1 == 'c')
    {
      servo_move_to(&ser3, grad, 5);
    }
    if (b1 == 'd')
    {
      servo_move_to(&ser4, grad, 5);
    }
     
    if ((pos + 4) < strlen(cmd))
    {
        pos = pos + 4;
    }
    else
    {
        pos = 0;
    }  
}
