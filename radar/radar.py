import serial
import sys
import time
import pygame
import math

data = [ "30 130", "40 10", "50 140", "60 140", "70 140", "80 130", "90 10", "100 140", "110 140", "120 140" ]

history = []
history_max_len = 8

#ser = serial.Serial(sys.argv[1], 9600, timeout=10)

window_width = 600
window_height = 600
window_center = [int(window_width / 2), int(window_height / 2)]

window = pygame.display.set_mode([window_width, window_height])

while True:
#    s = ser.readline()

    s = data.pop(0)
    data.append(s)

    a = s.split(' ')

    gradus = float(a[0])
    distance = float(a[1])

    v = pygame.math.Vector2()
    v.from_polar([distance * 2, gradus])

    history.append(v)
    if len(history) > history_max_len:
        history.pop(0)

    window.fill([0,0,0])

    i = 0
    while i < len(history):
      
        h = history[i]

        pos = [int(h[0]) + window_center[0], int(h[1]) + window_center[1]]
 
        color = [230 * (i + 1) / len(history) , 0, 0]

        pygame.draw.line(window, color, window_center, pos) 
        pygame.draw.circle(window, color, pos, 1)
 
        i = i + 1

    pygame.display.flip()    

    time.sleep(1)

#ser.close() 
