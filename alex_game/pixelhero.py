import pygame
import sys
import time

player_x = 77 * 2
player_y = 57 * 2
spritesheet = pygame.transform.scale2x(pygame.image.load('animation.gif'))

frames_jump_right = []
frames_jump_right.append(spritesheet.subsurface(pygame.Rect( player_x * 1,  player_y * 2, player_x, player_y)))
frames_jump_right.append(spritesheet.subsurface(pygame.Rect( player_x * 2,  player_y * 2, player_x, player_y)))
frames_jump_right.append(spritesheet.subsurface(pygame.Rect( player_x * 3,  player_y * 2, player_x, player_y)))
frames_jump_right.append(spritesheet.subsurface(pygame.Rect( player_x * 4,  player_y * 2, player_x, player_y)))
frames_jump_right.append(spritesheet.subsurface(pygame.Rect( player_x * 5,  player_y * 2, player_x, player_y)))
frames_jump_right.append(spritesheet.subsurface(pygame.Rect( player_x * 6,  player_y * 2, player_x, player_y)))
frames_jump_right.append(spritesheet.subsurface(pygame.Rect( player_x * 0,  player_y * 3, player_x, player_y)))
frames_jump_right.append(spritesheet.subsurface(pygame.Rect( player_x * 1,  player_y * 3, player_x, player_y)))
frames_jump_right.append(spritesheet.subsurface(pygame.Rect( player_x * 2,  player_y * 3, player_x, player_y)))

frames_jump_left = []
frames_jump_left.append(pygame.transform.flip(spritesheet.subsurface(pygame.Rect( player_x * 1,  player_y * 2, player_x, player_y)), True, False))
frames_jump_left.append(pygame.transform.flip(spritesheet.subsurface(pygame.Rect( player_x * 2,  player_y * 2, player_x, player_y)), True, False))
frames_jump_left.append(pygame.transform.flip(spritesheet.subsurface(pygame.Rect( player_x * 3,  player_y * 2, player_x, player_y)), True, False))
frames_jump_left.append(pygame.transform.flip(spritesheet.subsurface(pygame.Rect( player_x * 4,  player_y * 2, player_x, player_y)), True, False))
frames_jump_left.append(pygame.transform.flip(spritesheet.subsurface(pygame.Rect( player_x * 5,  player_y * 2, player_x, player_y)), True, False))
frames_jump_left.append(pygame.transform.flip(spritesheet.subsurface(pygame.Rect( player_x * 6,  player_y * 2, player_x, player_y)), True, False))
frames_jump_left.append(pygame.transform.flip(spritesheet.subsurface(pygame.Rect( player_x * 0,  player_y * 3, player_x, player_y)), True, False))
frames_jump_left.append(pygame.transform.flip(spritesheet.subsurface(pygame.Rect( player_x * 1,  player_y * 3, player_x, player_y)), True, False))
frames_jump_left.append(pygame.transform.flip(spritesheet.subsurface(pygame.Rect( player_x * 2,  player_y * 3, player_x, player_y)), True, False))

frames_stay_right = []
frames_stay_right.append(spritesheet.subsurface(pygame.Rect(player_x * 0, player_y * 0, player_x, player_y)))
frames_stay_right.append(spritesheet.subsurface(pygame.Rect(player_x * 1, player_y * 0, player_x, player_y)))
frames_stay_right.append(spritesheet.subsurface(pygame.Rect(player_x * 2, player_y * 0, player_x, player_y)))
frames_stay_right.append(spritesheet.subsurface(pygame.Rect(player_x * 3, player_y * 0, player_x, player_y)))

frames_stay_left = []
frames_stay_left.append(pygame.transform.flip(spritesheet.subsurface(pygame.Rect(player_x * 0, player_y * 0, player_x, player_y)), True, False))
frames_stay_left.append(pygame.transform.flip(spritesheet.subsurface(pygame.Rect(player_x * 1, player_y * 0, player_x, player_y)), True, False))
frames_stay_left.append(pygame.transform.flip(spritesheet.subsurface(pygame.Rect(player_x * 2, player_y * 0, player_x, player_y)), True, False))
frames_stay_left.append(pygame.transform.flip(spritesheet.subsurface(pygame.Rect(player_x * 3, player_y * 0, player_x, player_y)), True, False))

frames_run_right = []
frames_run_right.append(spritesheet.subsurface(pygame.Rect( player_x * 1,  player_y, player_x, player_y)))
frames_run_right.append(spritesheet.subsurface(pygame.Rect( player_x * 2,  player_y, player_x, player_y)))
frames_run_right.append(spritesheet.subsurface(pygame.Rect( player_x * 3,  player_y, player_x, player_y)))
frames_run_right.append(spritesheet.subsurface(pygame.Rect( player_x * 4,  player_y, player_x, player_y)))
frames_run_right.append(spritesheet.subsurface(pygame.Rect( player_x * 5,  player_y, player_x, player_y)))
frames_run_right.append(spritesheet.subsurface(pygame.Rect( player_x * 6,  player_y, player_x, player_y)))

frames_run_left = []
frames_run_left.append(pygame.transform.flip(spritesheet.subsurface(pygame.Rect( player_x * 1,  player_y, player_x, player_y)), True, False))
frames_run_left.append(pygame.transform.flip(spritesheet.subsurface(pygame.Rect( player_x * 2,  player_y, player_x, player_y)), True, False))
frames_run_left.append(pygame.transform.flip(spritesheet.subsurface(pygame.Rect( player_x * 3,  player_y, player_x, player_y)), True, False))
frames_run_left.append(pygame.transform.flip(spritesheet.subsurface(pygame.Rect( player_x * 4,  player_y, player_x, player_y)), True, False))
frames_run_left.append(pygame.transform.flip(spritesheet.subsurface(pygame.Rect( player_x * 5,  player_y, player_x, player_y)), True, False))
frames_run_left.append(pygame.transform.flip(spritesheet.subsurface(pygame.Rect( player_x * 6,  player_y, player_x, player_y)), True, False))

for f in frames_jump_right:
    f.set_colorkey(f.get_at((0,0)))
for f in frames_jump_left:
    f.set_colorkey(f.get_at((0,0)))
for f in frames_run_left:
    f.set_colorkey(f.get_at((0,0)))
for f in frames_stay_left:
    f.set_colorkey(f.get_at((0,0)))
for f in frames_run_right:
    f.set_colorkey(f.get_at((0,0)))
for f in frames_stay_right:
    f.set_colorkey(f.get_at((0,0)))


class PixelHero(pygame.sprite.Sprite):
    def __init__(self, base_x, base_y):

        pygame.sprite.Sprite.__init__(self)

        self.side = 'right'
        self.moving = False
        self.jumping = False
        self.jump_y = [0, -16, -32, -48, -64, -48, -32, -16, 0]

        self.base_x = base_x
        self.base_y = base_y
        self.x = base_x
        self.y = base_y
        self.dx = 0
        self.dy = 0

        self.frames = None
        self.frame_index = 0

        self.update()

    def process_event(self, scene, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            self.moving = True
            self.side = 'right'
        if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            self.moving = True
            self.side = 'left'
        if event.type == pygame.KEYUP and event.key == pygame.K_a:
            self.moving = False
            self.side  = 'left'
        if event.type == pygame.KEYUP and event.key == pygame.K_d:
            self.moving = False
            self.side  = 'right'
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            self.jumping = True


    def update(self):

        old_frames = self.frames

        if self.jumping:
            if self.side == 'right':
                self.frames = frames_jump_right
            if self.side == 'left':
                self.frames = frames_jump_left
        elif self.moving:
            if self.side == 'right':
                self.frames = frames_run_right
            if self.side == 'left':
                self.frames = frames_run_left
        else:
            if self.side == 'right':
                self.frames = frames_stay_right
            if self.side == 'left':
                self.frames = frames_stay_left

        if old_frames != self.frames:
            self.frame_index = 0
        else:
            self.frame_index += 1

        if self.frame_index >= len(self.frames):
            self.frame_index = 0

        self.dx = 0
        self.dy = 0

        if self.moving:
            if self.side == 'left':
                self.dx = -20
            if self.side == 'right':
                self.dx = 20

        if self.jumping:
            self.dy = self.jump_y[self.frame_index]
            if self.frame_index == (len(self.frames) - 1):
                self.jumping = False

        self.x += self.dx
        self.y = self.base_y + self.dy

        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y