import pygame, os
import level1

size = 40
speed = 3
current_path = os.path.dirname(__file__) # Where your .py file is located
resource_path = os.path.join(current_path, 'assets') # The resource folder path
image_path = os.path.join(resource_path, 'bobby') # The image folder path

class Player(object):
    def __init__(self):
        self.image = pygame.image.load(os.path.join(image_path, 'Bobby.png'))
        self.bobby = pygame.Rect(level1.playerPosX, level1.playerPosY, size, size)
        # self.rect = pygame.Rect(level1.playerPosX, level1.playerPosY, size, size)

    def move(self, dx, dy):
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)

    def move_single_axis(self, dx, dy):
        # Mueve a bobby
        self.bobby.x += dx
        self.bobby.y += dy
        level1.colision(dx, dy)
