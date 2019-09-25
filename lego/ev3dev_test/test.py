#!/usr/bin/env python3

import time
import sys
from ev3dev2.motor import LargeMotor, OUTPUT_A
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.sensor import INPUT_1

m = LargeMotor(OUTPUT_A)

t = TouchSensor(INPUT_1)

for i in range(10):
    print(t.value(), file=sys.stderr)
    print(t.value())
    time.sleep(1)

m.on_to_position(10, 90)
time.sleep(2)
m.on_to_position(10, 180)
time.sleep(2)
m.on_to_position(10, 90)
time.sleep(2)

print('vse konchilos', file=sys.stderr)




