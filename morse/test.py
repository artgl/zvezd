import pygame
import time
import sys

pygame.init()
screen = pygame.display.set_mode((100, 100))
clock = pygame.time.Clock()

prev_state = False

key_down_time = None
key_up_time = None
dot_duration = None

letter = []

print("Используйте клавишу z чтобы передать сообщение азбукой морзе")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)

    keys = pygame.key.get_pressed()
    state = keys[pygame.K_z]

    if prev_state != state:
        # состояние клавиши изменилось
        if state:
            # кнопка нажата
            key_down_time = time.time()
            if len(letter) > 0:
                # это уже не первое нажатие. проверяем длительность паузы, и если она значительно короче 
                # текущей длины точки, то устанавливаем длительность точки равной длительности 
                # измеренной паузы.
                duration = key_down_time - key_up_time

                print("duration", duration)

                if duration * 2.3 < dot_duration:
                    dot_duration = duration

                # постоянно слегка меняем длительнсть точки в зависимости от последней измеренной паузы
                dot_duration = (2.0 / 3) * dot_duration + (1.0 / 3) * duration

        else:
            # кнопка отпущена
            key_up_time = time.time()
            duration = key_up_time - key_down_time
            if dot_duration is None:
                # мы получили длительность первого символа. считаем что это была точка
                dot_duration = duration
            letter.append(duration)

    if key_up_time:
        # если с момента отпускания клавиши прошло более 4х интервалов (интервал это длина точки),
        # то буква закончилась
        if (time.time() - key_up_time) > (5 * dot_duration):
            if len(letter) > 0:
                print("dot_duration: ", dot_duration)
                print("letter: ", end='')
                for duration in letter:
                    print("_" if duration > 1.5 * dot_duration else ".", end='')
                print(" ", letter)
                        
                letter = []

    prev_state = state


    clock.tick(20)
