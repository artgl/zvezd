import pygame
import sys
from settings import lazurit
from settings import transparent
from settings import size, white
import time

pygame.init()
pygame.display.set_caption('ny sho govno, opyat\' nazralsya?')

screen = pygame.display.set_mode(size)

background = pygame.transform.scale(pygame.image.load('hqdefault.jpg'),size)

player_x = 77 * 2
player_y = 57 * 2

spritesheet = pygame.transform.scale2x(pygame.image.load('animation.gif'))
player = spritesheet.subsurface(pygame.Rect(player_x * 1,  player_y, player_x, player_y))

frames = []
frames.append(spritesheet.subsurface(pygame.Rect( player_x * 1,  player_y, player_x, player_y)))
frames.append(spritesheet.subsurface(pygame.Rect( player_x * 2,  player_y, player_x, player_y)))
frames.append(spritesheet.subsurface(pygame.Rect( player_x * 3,  player_y, player_x, player_y)))
frames.append(spritesheet.subsurface(pygame.Rect( player_x * 4,  player_y, player_x, player_y)))
frames.append(spritesheet.subsurface(pygame.Rect( player_x * 5,  player_y, player_x, player_y)))
frames.append(spritesheet.subsurface(pygame.Rect( player_x * 6,  player_y, player_x, player_y)))
for f in frames:
    f.set_colorkey(f.get_at((0,0)))
moving = False
i = 0
z = (0, 440)


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
        if event.type == pygame.KEYUP and event.key == pygame.K_d:
            moving = False

    if moving == True:
        z = (z[0] + 10, z[1])

    if z[0] > size[0]:
        screen.blit(text, (size[0] / 2 - 400, size[1] / 2 - 100))
        pygame.display.flip()
        continue

    i = i + 1

    if i >= len(frames):
        i = 0

    pygame.mouse.set_visible(False)

    screen.blit(background,(0,0))
#    screen.blit(img, z)
    screen.blit(frames[i], z)
    time.sleep(0.1)
    pygame.display.flip()
