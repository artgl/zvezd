import cv2
import numpy as np

img = cv2.imread('image.jpg')

x = 700
y = 300

cv2.circle(img, (x, y), 10, (255, 0, 0), -1)

cv2.imshow('window1', img)

color = img[y, x]
print(color)
print("blue:  " + str(color[0]))
print("green: " + str(color[1]))
print("red:   " + str(color[2]))

# loop while window is visible
while True:
    cv2.waitKey(50)
    if cv2.getWindowProperty('window1', cv2.WND_PROP_VISIBLE) < 1:
        break

color1 = np.array([150, 0, 0])
color2 = np.array([255, 255, 255])

mask = cv2.inRange(img, color1, color2)

color = mask[y, x]
print(color)

cv2.imshow('window1', mask)

# loop while window is visible
while True:
    cv2.waitKey(50)
    if cv2.getWindowProperty('window1', cv2.WND_PROP_VISIBLE) < 1:
        break
