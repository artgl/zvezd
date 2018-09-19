import pygame
import sys
import time
from settings import lazurit
from settings import transparent
from settings import size, white


pygame.init()
pygame.display.set_caption('ny sho govno, opyat\' nazralsya?')
screen = pygame.display.set_mode(size)
background = pygame.transform.scale(pygame.image.load('hqdefault.jpg'),size)
img = pygame.transform.scale2x(pygame.image.load('Untitled.gif'))
img.set_colorkey(img.get_at((0,0)))

player_x = 77 * 2
player_y = 57 * 2

spritesheet = pygame.transform.scale2x(pygame.image.load('animation.gif'))
player = spritesheet.subsurface(pygame.Rect(player_x * 1,  player_y, player_x, player_y))

frames_jump = []
frames_jump.append(spritesheet.subsurface(pygame.Rect( player_x * 1,  player_y * 2, player_x, player_y)))
frames_jump.append(spritesheet.subsurface(pygame.Rect( player_x * 2,  player_y * 2, player_x, player_y)))
frames_jump.append(spritesheet.subsurface(pygame.Rect( player_x * 3,  player_y * 2, player_x, player_y)))
frames_jump.append(spritesheet.subsurface(pygame.Rect( player_x * 4,  player_y * 2, player_x, player_y)))
frames_jump.append(spritesheet.subsurface(pygame.Rect( player_x * 5,  player_y * 2, player_x, player_y)))
frames_jump.append(spritesheet.subsurface(pygame.Rect( player_x * 6,  player_y * 2, player_x, player_y)))
frames_jump.append(spritesheet.subsurface(pygame.Rect( player_x * 0,  player_y * 3, player_x, player_y)))
frames_jump.append(spritesheet.subsurface(pygame.Rect( player_x * 1,  player_y * 3, player_x, player_y)))
frames_jump.append(spritesheet.subsurface(pygame.Rect( player_x * 2,  player_y * 3, player_x, player_y)))

frames_stay = []
frames_stay.append(spritesheet.subsurface(pygame.Rect(player_x * 0, player_y * 0, player_x, player_y)))
frames_stay.append(spritesheet.subsurface(pygame.Rect(player_x * 1, player_y * 0, player_x, player_y)))
frames_stay.append(spritesheet.subsurface(pygame.Rect(player_x * 2, player_y * 0, player_x, player_y)))
frames_stay.append(spritesheet.subsurface(pygame.Rect(player_x * 3, player_y * 0, player_x, player_y)))

frames_run = []
frames_run.append(spritesheet.subsurface(pygame.Rect( player_x * 1,  player_y, player_x, player_y)))
frames_run.append(spritesheet.subsurface(pygame.Rect( player_x * 2,  player_y, player_x, player_y)))
frames_run.append(spritesheet.subsurface(pygame.Rect( player_x * 3,  player_y, player_x, player_y)))
frames_run.append(spritesheet.subsurface(pygame.Rect( player_x * 4,  player_y, player_x, player_y)))
frames_run.append(spritesheet.subsurface(pygame.Rect( player_x * 5,  player_y, player_x, player_y)))
frames_run.append(spritesheet.subsurface(pygame.Rect( player_x * 6,  player_y, player_x, player_y)))

for f in frames_jump:
    f.set_colorkey(f.get_at((0,0)))
for f in frames_run:
    f.set_colorkey(f.get_at((0,0)))
for f in frames_stay:
    f.set_colorkey(f.get_at((0,0)))

moving = False
i = 0
z = (0, 440)
base_x = (0)
base_y =(440)
frames = frames_stay
jumping = 0
jump_y = [0,16,32,48,64,48,32,16,0]
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 160)
text = myfont.render('GAME OVER', False, (220, 0, 0))
text_rect = text.get_rect()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        screen.fill(white)

        if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            moving = True
            frames = frames_run
            distance = 20
        if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            moving = True
            frames = frames_run
            distance = -20
        if event.type == pygame.KEYUP and event.key == pygame.K_a:
            moving = False
            frames = frames_stay
        if event.type == pygame.KEYUP and event.key == pygame.K_d:
            moving = False
            frames = frames_stay
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            jumping = True
            frames = frames_jump
        if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            z = (z[0], 440)
            moving = False



    if jumping:
        z = (z[0], base_y - jump_y[i])








    if moving:
        z = (z[0] + distance, z[1])

    if z[0] > size[0]:
        screen.blit(text, (size[0] / 2 - 400, size[1] / 2 - 100))
        pygame.display.flip()
        continue


    i = i + 1
    if i >= len(frames):
        if jumping:
            jumping = False
            frames = frames_stay
        i = 0

    pygame.mouse.set_visible(False)
    screen.blit(background, (0, 0))
    screen.blit(frames[i], z)


    time.sleep(0.1)
    pygame.display.flip()