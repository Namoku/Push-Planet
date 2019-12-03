import sys
sys.path.insert(1, 'source/')
import pygame, os
import level1

size = 40
speed = 4
current_path = os.path.dirname(__file__) # Where your .py file is located
resource_path = os.path.join(current_path, '../assets') # The resource folder path
image_path = os.path.join(resource_path, 'bobby') # The image folder path

class Player(pygame.sprite.Sprite):
    def __init__(self, position):
        self.bobby = pygame.Rect(level1.playerPosX, level1.playerPosY, 27, 40)
        self.sheet = pygame.image.load(os.path.join(image_path, 'bobby.png'))
        self.sheet.set_clip(pygame.Rect(0, 0, 40, 40))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.frame = 0
        self.left_states = { 0: (40, 120, 40, 40), 1: (0, 120, 40, 40), 2: (40, 120, 40, 40), 3: (40, 120, 40, 40) }
        self.right_states = { 0: (0, 80, 40, 40), 1: (40, 80, 40, 40), 2: (0, 80, 40, 40), 3: (0, 80, 40, 40) }
        self.up_states = { 0: (0, 40, 40, 40), 1: (40, 40, 40, 40), 2: (0, 40, 40, 40), 3: (0, 40, 40, 40) }
        self.down_states = { 0: (0, 0, 40, 40), 1: (40, 0, 40, 40), 2: (0, 0, 40, 40), 3: (0, 0, 40, 40) }
        self.colorImg = pygame.image.load(os.path.join(image_path, 'bobby_dmg.png'))
        self.estadoDa = False
        self.n = 0

    def animacionVida(self, screen):
        if self.estadoDa:
            self.estadoDa = False
            self.n = 1
        elif self.n > 20:
            self.n  = 0
        elif self.n >= 1:
            self.n += 1
            if self.n % 2 == 0:
                screen.blit(self.colorImg, (self.bobby.x-6, self.bobby.y))


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


    def move(self, direction, especial):
        if direction == 'left':
            self.clip(self.left_states)
            self.move_single_axis(-speed, 0, especial)
        if direction == 'right':
            self.clip(self.right_states)
            self.move_single_axis(speed, 0, especial)
        if direction == 'up':
            self.clip(self.up_states)
            self.move_single_axis(0, -speed, especial)
        if direction == 'down':
            self.clip(self.down_states)
            self.move_single_axis(0, speed, especial)

        if direction == 'stand_left':
            self.clip(self.left_states[0])
        if direction == 'stand_right':
            self.clip(self.right_states[0])

        self.image = self.sheet.subsurface(self.sheet.get_clip())

    def move_single_axis(self, dx, dy, especial):
        # Mueve a bobby
        self.bobby.x += dx
        self.bobby.y += dy
        level1.caja.caja1HitBox.x = level1.caja.caja1.x - 5
        level1.caja.caja2HitBox.x = level1.caja.caja2.x - 5
        level1.caja.caja3HitBox.x = level1.caja.caja3.x - 5
        level1.caja.caja1HitBox.y = level1.caja.caja1.y - 5
        level1.caja.caja2HitBox.y = level1.caja.caja2.y - 5
        level1.caja.caja3HitBox.y = level1.caja.caja3.y - 5
        level1.colision(dx, dy, especial)

class Humo(pygame.sprite.Sprite):
    def __init__(self):
        self.sheet = pygame.image.load(os.path.join(image_path, 'humo.png'))
        self.sheet.set_clip(pygame.Rect(0, 0, 40, 40))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0)
        self.frame = 0
        self.states = { 0: (0, 0, 40, 40), 1: (40, 0, 40, 40), 2: (80, 0, 40, 40), 3: (120, 0, 40, 40), 4: (160, 0, 40, 40) }
        self.animaciones = 0
        self.terminado = True

    def get_frame(self, frame_set):
        if self.animaciones > 4:
            self.frame += 1
            self.animaciones = 0
        else:
            self.animaciones += 1
        if self.frame > (len(frame_set) - 1):
            self.terminado = True
            self.frame = 0
        return frame_set[self.frame]

    def clip(self, clipped_rect):
        if type(clipped_rect) is dict:
            self.sheet.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
        else:
            self.sheet.set_clip(pygame.Rect(clipped_rect))
        return clipped_rect

    def animacion(self, screen):
        screen.blit(self.image, self.rect)
        self.clip(self.states)
        self.image = self.sheet.subsurface(self.sheet.get_clip())
