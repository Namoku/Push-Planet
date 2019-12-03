import sys
sys.path.insert(1, 'source/')
import pygame, os
import level3, level1

size = 40
current_path = os.path.dirname(__file__) # Where your .py file is located
resource_path = os.path.join(current_path, '../assets') # The resource folder path
image_path = os.path.join(resource_path, 'bobby') # The image folder path

class Monster(pygame.sprite.Sprite):
    def __init__(self, position):
        self.bobby = pygame.Rect(level3.enemigoPosX, level3.enemigoPosY, 39, 40)
        self.sheet = pygame.image.load(os.path.join(image_path, 'enemigo.png'))
        self.sheet.set_clip(pygame.Rect(0, 0, 40, 40))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.frame = 0
        self.up_states = { 0: (0, 40, 40, 40), 1: (40, 40, 40, 40), 2: (80, 40, 40, 40) }
        self.down_states = { 0: (0, 0, 40, 40), 1: (40, 0, 40, 40), 2: (80, 0, 40, 40) }

    def get_frame(self, frame_set):
        self.frame += 1
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
        return frame_set[self.frame]

    def clip(self, clipped_rect):
        if type(clipped_rect) is dict:
            self.sheet.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
        else:
            self.sheet.set_clip(pygame.Rect(clipped_rect))
        return clipped_rect


    def move(self, direction, speedx, speedy):
        if direction == 'up':
            self.clip(self.down_states)
            self.move_single_axis(speedx, speedy)
        if direction == 'down':
            self.clip(self.down_states)
            self.move_single_axis(0, speedy)
        if direction == 'right':
            self.clip(self.down_states)
            self.move_single_axis(speedx, 0)
        if direction == 'left':
            self.clip(self.down_states)
            self.move_single_axis(-speedx, 0)
        if self.bobby.colliderect(level3.player.bobby):
            level1.humo3.terminado = False
            level1.humo3.rect.x = self.bobby.x
            level1.humo3.rect.y = self.bobby.y
            level3.vida -= 100
            self.bobby.x = level1.enemigoPosX
            self.bobby.y = level1.enemigoPosY
            level1.humo4.terminado = False
            level1.humo4.rect.x = self.bobby.x
            level1.humo4.rect.y = self.bobby.y
            level3.player.estadoDa = True

        self.image = self.sheet.subsurface(self.sheet.get_clip())

    def move_single_axis(self, dx, dy):
        # Mueve a bobby
        self.bobby.x += dx
        self.bobby.y += dy
        level3.colisionEnemigo(dx, dy)
