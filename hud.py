import pygame, os
from pygame.locals import *
# Path
current_path = os.path.dirname(__file__)  # Where your .py file is located
resource_path = os.path.join(current_path, 'assets')  # The resource folder path
image_path = os.path.join(resource_path, 'level')  # The image folder path


barra = pygame.image.load(os.path.join(image_path, 'hud.png'))
cesto = pygame.image.load(os.path.join(image_path, 'cesto.png'))
lata = pygame.image.load(os.path.join(image_path, 'lata.png'))
palomita = pygame.image.load(os.path.join(image_path, 'check.png'))
vida = pygame.image.load(os.path.join(image_path, 'hearth.png'))
igual = pygame.image.load(os.path.join(image_path, 'equal.png'))
barra2 = pygame.image.load(os.path.join(image_path, 'hud2.png'))
