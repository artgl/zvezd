#!/usr/bin/env python3
import sys
import math
from ev3dev2.motor import LargeMotor, OUTPUT_C, OUTPUT_D, OUTPUT_B
from ev3dev2.sensor.lego import UltrasonicSensor
from ev3dev2.sound import Sound

import time
from ev3dev2.sound import Sound
m1 = LargeMotor(OUTPUT_C)
m2 = LargeMotor(OUTPUT_D)
m3 = LargeMotor(OUTPUT_B)

us = UltrasonicSensor()
sound = Sound()

print(us.distance_centimeters, file=sys.stderr)


a_min = m3.position + 10
m3.on(-10, block=False)
while m3.position < a_min:
    a_min = m3.position
    time.sleep(0.1)
m3.off()
print("a_min", a_min, file=sys.stderr)

a_max = m3.position - 10
m3.on(10, block=False)
while m3.position > a_max:
    a_max = m3.position
    time.sleep(0.1)
m3.off()
print("a_max", a_max, file=sys.stderr)


def zahvat(a_min, a_max):
    a = a_min
    m3.on(-10, block=False)
    while abs(m3.position - a) > 1:
        a = m3.position
        time.sleep(0.1)
    m3.off()

def otpusk(a_min, a_max):
    a = a_max
    m3.on(10, block=False)
    while abs(m3.position - a) > 1:
        a = m3.position
        time.sleep(0.1)
    m3.off()

t1 = time.time()
m1.on(-10, block=False)
m2.on(-10, block=False)
while us.distance_centimeters > 4:
    print(us.distance_centimeters, file=sys.stderr)
    time.sleep(0.1)
m1.on_for_seconds(-10, 0.5, block=False)
m2.on_for_seconds(-10, 0.5, block=False)
time.sleep(0.5)
t2 = time.time()
m1.off()
m2.off()

sound.speak('TI MNE MESHAYESH')

zahvat(a_min, a_max)

m1.on_for_seconds(-10, 2, block=False)
m2.on_for_seconds(10, 2, block=False)
time.sleep(2)

otpusk(a_min, a_max)

m1.on_for_seconds(10, 2, block=False)
m2.on_for_seconds(-10, 2, block=False)
time.sleep(2)

m1.on_for_seconds(-10, 2, block=False)
m2.on_for_seconds(-10, 2, block=False)
time.sleep(2)

sys.exit()

m1.on(10, block=False)
m2.on(10, block=False)
t3 = time.time()
while time.time() < t3 + (t2 - t1): 
    time.sleep(0.1)
m1.off()
m2.off()


