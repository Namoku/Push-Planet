import sys
sys.path.insert(1, 'source/')
import pygame, os

# Path
current_path = os.path.dirname(__file__)  # Where your .py file is located
resource_path = os.path.join(current_path, '../assets')  # The resource folder path
image_path = os.path.join(resource_path, 'menu')  # The image folder path

#Clases y metodos
class Background(pygame.sprite.Sprite):
    def __init__(self, location):
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image = pygame.image.load(os.path.join(image_path, 'bg_menu.png'))
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
BackGround = Background((0,0))


play = pygame.image.load(os.path.join(image_path, 'play.png'))
options = pygame.image.load(os.path.join(image_path, 'options.png'))
exit = pygame.image.load(os.path.join(image_path, 'exit.png'))
logo = pygame.image.load(os.path.join(image_path, 'logo.png'))
level1 = pygame.image.load(os.path.join(image_path, 'level1.png'))
level2 = pygame.image.load(os.path.join(image_path, 'level2.png'))
level3 = pygame.image.load(os.path.join(image_path, 'level3.png'))
pausa = pygame.image.load(os.path.join(image_path, 'pausa.png'))
restart = pygame.image.load(os.path.join(image_path, 'restart.png'))
continuar = pygame.image.load(os.path.join(image_path, 'continue.png'))
opciones = pygame.image.load(os.path.join(image_path, 'opciones.png'))
volumen1 = pygame.image.load(os.path.join(image_path, 'volumen.png'))
volumen2 = pygame.image.load(os.path.join(image_path, 'volumen2.png'))
bg_death = pygame.image.load(os.path.join(image_path, 'bg_death.png'))
gameover = pygame.image.load(os.path.join(image_path, 'gameover.png'))

def Bordes(screen, pos):
    color = (0, 0, 0)
    pos[0] -= 4
    pos[1] -= 4
    pygame.draw.rect(screen, color, (pos[0], pos[1], 208, 4))
    pygame.draw.rect(screen, color, (pos[0], pos[1] + 104, 208, 4))
    pygame.draw.rect(screen, color, (pos[0], pos[1], 4, 108))
    pygame.draw.rect(screen, color, (pos[0] + 204, pos[1], 4, 108))

def Bordes2(screen, pos):
    color = (0, 0, 0)
    pos[0] -= 4
    pos[1] -= 4
    pygame.draw.rect(screen, color, (pos[0], pos[1], 258, 4))
    pygame.draw.rect(screen, color, (pos[0], pos[1] + 254, 258, 4))
    pygame.draw.rect(screen, color, (pos[0], pos[1], 4, 258))
    pygame.draw.rect(screen, color, (pos[0] + 254, pos[1], 4, 254))

def Ciclo1(n):
    if n > 1:
        n = 0
    else:
        n += 1
    return n
def Ciclo2(n):
    if n < 1:
        n = 2
    else:
        n -= 1
    return n
