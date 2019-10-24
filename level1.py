from player import *

playerPosX = 680
playerPosY = 480
caja1PosX = 440
caja1PosY = 520
caja2PosX = 480
caja2PosY = 520
bote1PosX = 320
bote1PosY = 40
bote2PosX = 360
bote2PosY = 40



def restart():
    player.bobby.x = playerPosX
    player.bobby.y = playerPosY
    caja.caja1.x = caja1PosX
    caja.caja1.y = caja1PosY
    caja.caja2.x = caja2PosX
    caja.caja2.y = caja2PosY


current_path = os.path.dirname(__file__)  # Where your .py file is located
resource_path = os.path.join(current_path, 'assets')  # The resource folder path
image_path = os.path.join(resource_path, 'level')  # The image folder path


class Background(pygame.sprite.Sprite):
    def __init__(self, location):
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image = pygame.image.load(os.path.join(image_path, 'fondo.png'))
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


class Wall(object):
    def __init__(self, pos):
        walls.append(self)
        self.image = pygame.image.load(os.path.join(image_path, 'level.png'))
        self.rect = pygame.Rect(pos[0], pos[1], size, size)


class Caja(object):
    def __init__(self):
        self.caja1 = pygame.Rect(caja1PosX, caja1PosY, size, size)
        self.caja2 = pygame.Rect(caja2PosX, caja2PosY, size, size)


class Vacio(object):
    def __init__(self, pos):
        vacios.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], size, size)

class Bote(object):
    def __init__(self):
        self.bote1 = pygame.Rect(bote1PosX, bote1PosY, size, size)
        self.bote2 = pygame.Rect(bote2PosX, bote2PosY, size, size)


walls = []  # Paredes
player = Player()  # Crear jugador
caja = Caja()
vacios = []
bote = Bote()

level = [
    "WWWWWWWWWWWWWWWWWW",
    "W  W  W   W WWWW W",
    "W  W  W W   WWWW W",
    "W       WWW WWWW W",
    "W      WWWW      W",
    "WWWWWW WWWW      W",
    "W    W       WW  W",
    "W W  W  WWWWWWW  W",
    "W WW W   WWWWWW  W",
    "W W  W       WW  W",
    "W W           WW W",
    "W WWWWWWWWW      W",
    "W W        W    WW",
    "W W   WWWWWWW    W",
    "W W   WWWWWWWWW  W",
    "W WW             W",
    "W        W  WWW  W",
    "WWWWWWWWWWWWWWWWWW"
]

# Convertir cadena a nivel
x = 280
y = 0
for row in level:
    for col in row:
        if col == "W":
            Wall((x, y))
        if col == "E":
            end_rect = pygame.Rect(x, y, size, size)
        if col == " ":
            Vacio((x, y))
        x += size
    y += size
    x = 280


def colision(dx, dy):
    for wall in walls:
        if player.bobby.colliderect(wall.rect):
            if dx > 0:  # Moving right; Hit the left side of the wall
                player.bobby.right = wall.rect.left
            if dx < 0:  # Moving left; Hit the right side of the wall
                player.bobby.left = wall.rect.right
            if dy > 0:  # Moving down; Hit the top side of the wall
                player.bobby.bottom = wall.rect.top
            if dy < 0:  # Moving up; Hit the bottom side of the wall
                player.bobby.top = wall.rect.bottom
        if caja.caja1.colliderect(wall.rect):
            if dx > 0:  # No dejar pasar la caja desde izquierda
                caja.caja1.x -= speed
                player.bobby.x -= speed
            if dx < 0:  # # No dejar pasar la caja desde derecha
                caja.caja1.x += speed
                player.bobby.x += speed
            if dy > 0:  # No dejar pasar la caja desde arriba
                caja.caja1.y -= speed
                player.bobby.y -= speed
            if dy < 0:  # No dejar pasar la caja desde abajo
                caja.caja1.y += speed
                player.bobby.y += speed
        if caja.caja2.colliderect(wall.rect):
            if dx > 0:  # No dejar pasar la caja desde izquierda
                caja.caja2.x -= speed
                player.bobby.x -= speed
            if dx < 0:  # # No dejar pasar la caja desde derecha
                caja.caja2.x += speed
                player.bobby.x += speed
            if dy > 0:  # No dejar pasar la caja desde arriba
                caja.caja2.y -= speed
                player.bobby.y -= speed
            if dy < 0:  # No dejar pasar la caja desde abajo
                caja.caja2.y += speed
                player.bobby.y += speed
        if caja.caja1.colliderect(caja.caja2):
            if dx > 0:  # No dejar pasar la caja desde izquierda
                caja.caja1.x -= speed
                player.bobby.x -= speed
            if dx < 0:  # # No dejar pasar la caja desde derecha
                caja.caja1.x += speed
                player.bobby.x += speed
            if dy > 0:  # No dejar pasar la caja desde arriba
                caja.caja1.y -= speed
                player.bobby.y -= speed
            if dy < 0:  # No dejar pasar la caja desde abajo
                caja.caja1.y += speed
                player.bobby.y += speed

        else:
            if player.bobby.colliderect(caja.caja1):
                if dx > 0 or dx < 0:
                    caja.caja1.x += dx
                if dy > 0 or dy < 0:
                    caja.caja1.y += dy
            if player.bobby.colliderect(caja.caja2):
                if dx > 0 or dx < 0:
                    caja.caja2.x += dx
                if dy > 0 or dy < 0:
                    caja.caja2.y += dy
