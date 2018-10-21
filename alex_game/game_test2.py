import pygame
import sys
from threading import Timer

from pixelhero import PixelHero

size = (1024, 768)

class Background(pygame.sprite.Sprite):
    def __init__(self, size, color):
        pygame.sprite.Sprite.__init__(self)
#        self.image = pygame.transform.scale(pygame.image.load('hqdefault.jpg'), size)
        self.image = pygame.Surface(size)
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect = self.image.get_rect()

class Text(pygame.sprite.Sprite):
    def __init__(self, text, x=0, y=0):
        pygame.sprite.Sprite.__init__(self)

        self.text = text
        self.cur_width = 0
        self.rect = pygame.Rect(x,y,0,0)

        myfont = pygame.font.SysFont('Comic Sans MS', 80)
        self.orig_image = myfont.render(text, False, (220, 0, 0))

        self.update()

    def update(self):
        self.image = self.orig_image.subsurface(pygame.Rect(0, 0, self.cur_width, self.orig_image.get_height()))
        if self.cur_width < self.orig_image.get_width():
            self.cur_width += 1
        self.rect.width = self.image.get_width()
        self.rect.height = self.image.get_height()
        if self.rect.x < 500:
            self.rect.x += 1
        else:
            self.rect.x = 0


pygame.init()
pygame.font.init()

pygame.display.set_caption('Alex Game')
screen = pygame.display.set_mode(size)

player = PixelHero(base_x=100, base_y=300)

background1 = Background(size, (0, 0, 0))

background2 = Background(size, (100, 100, 100))

scene1 = pygame.sprite.LayeredUpdates()
scene1.add(background1, layer=1)
scene1.add(player, layer=3)

scene2 = pygame.sprite.LayeredUpdates()
scene2.add(background2, layer=1)
scene2.add(player, layer=3)

scene = scene1

event1 = pygame.event.Event(pygame.USEREVENT + 1)
event2 = pygame.event.Event(pygame.USEREVENT + 2)

clock = pygame.time.Clock()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        if event.type == (pygame.USEREVENT + 1):
            scene = scene1
        if event.type == (pygame.USEREVENT + 2):
            scene = scene2
        player.process_event(scene, event)

    scene.update()
    scene.draw(screen)

    pygame.display.flip()

    clock.tick(15)
