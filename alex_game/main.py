import pygame
import sys
from threading import Timer

size = (1440, 600)

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

class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, dx):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((5, 5))
        self.image.fill((200, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.dx = dx

    def update(self):
        self.rect.x += self.dx

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, keynumber):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((100, 100))
        self.image.fill((0, 200, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.keynumber = keynumber
        self.dx = 0
        self.dy = 0

    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy
        if self.rect.x <= 0:
            self.rect.x = 0
        if self.rect.x >= 1340:
            self.rect.x = 1340
        if self.rect.y <= 0:
            self.rect.y = 0
        if self.rect.y >= 500:
            self.rect.y = 500
    def process_event(self, scene, event):

        if self.keynumber == 1:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                self.dx = -10
            if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
                self.dx = 10
            if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
                self.dy = -10
            if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                self.dy = 10
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                pt = Projectile(x=self.rect.x + 50, y=self.rect.y + 50, dx=20)
                scene.add(pt, layer=10)

            if event.type == pygame.KEYUP and event.key == pygame.K_a:
                self.dx = 0
            if event.type == pygame.KEYUP and event.key == pygame.K_d:
                self.dx = 0
            if event.type == pygame.KEYUP and event.key == pygame.K_w:
                self.dy = 0
            if event.type == pygame.KEYUP and event.key == pygame.K_s:
                self.dy = 0

        if self.keynumber == 2:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_KP4:
                self.dx = -10
            if event.type == pygame.KEYDOWN and event.key == pygame.K_KP6:
                self.dx = 10
            if event.type == pygame.KEYDOWN and event.key == pygame.K_KP8:
                self.dy = -10
            if event.type == pygame.KEYDOWN and event.key == pygame.K_KP5:
                self.dy = 10

            if event.type == pygame.KEYUP and event.key == pygame.K_KP4:
                self.dx = 0
            if event.type == pygame.KEYUP and event.key == pygame.K_KP6:
                self.dx = 0
            if event.type == pygame.KEYUP and event.key == pygame.K_KP8:
                self.dy = 0
            if event.type == pygame.KEYUP and event.key == pygame.K_KP5:
                self.dy = 0

            if event.type == pygame.KEYDOWN and event.key == pygame.K_KP_ENTER:
                pt = Projectile(x=self.rect.x + 50, y=self.rect.y + 50, dx=-20)
                scene.add(pt, layer=10)



pygame.init()
pygame.font.init()

pygame.display.set_caption('Alex Game')
screen = pygame.display.set_mode(size)

player = Player(keynumber = 1, x = 300, y = 300)

player2 = Player(keynumber = 2,x = 900,y = 300)

text1 = Text('oopsssss', 100, 100)
background1 = Background(size, (0, 0, 0))

text2 = Text('hello')
background2 = Background(size, (100, 100, 100))

scene1 = pygame.sprite.LayeredUpdates()
scene1.add(background1, layer=1)
scene1.add(text1, layer=2)
scene1.add(player, layer=3)
scene1.add(player2, layer=3)

scene2 = pygame.sprite.LayeredUpdates()
scene2.add(background2, layer=1)
scene2.add(text2, layer=2)
scene2.add(player, layer=3)
scene2.add(player2, layer=3)

scene = scene1

event1 = pygame.event.Event(pygame.USEREVENT + 1)
event2 = pygame.event.Event(pygame.USEREVENT + 2)

Timer(5, lambda: pygame.event.post(event2)).start()
Timer(10, lambda: pygame.event.post(event1)).start()

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
        player2.process_event(scene, event)

    print(len(scene.sprites()))

    scene.update()
    scene.draw(screen)

    pygame.display.flip()

    clock.tick(30)
