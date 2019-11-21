from player import *

playerPosX = 680
playerPosY = 480
caja1PosX = 440
caja1PosY = 520
caja2PosX = 480
caja2PosY = 520
caja3PosX = 520
caja3PosY = 520
bote1PosX = 320
bote1PosY = 40
bote2PosX = 360
bote2PosY = 40
trashSize = 20



def restart():
    player.bobby.x = playerPosX
    player.bobby.y = playerPosY
    caja.caja1.x = caja1PosX
    caja.caja1.y = caja1PosY
    caja.caja2.x = caja2PosX
    caja.caja2.y = caja2PosY
    caja.caja3.x = caja3PosX
    caja.caja3.y = caja3PosY


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
        self.caja1 = pygame.Rect(caja1PosX, caja1PosY, trashSize, trashSize)
        self.caja2 = pygame.Rect(caja2PosX, caja2PosY, trashSize, trashSize)
        self.caja3 = pygame.Rect(caja3PosX, caja3PosY, trashSize, trashSize)
        self.caja1HitBox = pygame.Rect(caja1PosX - 2, caja1PosY - 2, trashSize + 10, trashSize + 10)
        self.caja2HitBox = pygame.Rect(caja2PosX - 2, caja2PosY - 2, trashSize + 10, trashSize + 10)
        self.caja3HitBox = pygame.Rect(caja3PosX - 2, caja3PosY - 2, trashSize + 10, trashSize + 10)


class Vacio(object):
    def __init__(self, pos):
        vacios.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], size, size)

class Bote(object):
    def __init__(self):
        self.bote1 = pygame.Rect(bote1PosX, bote1PosY, size, size)
        self.bote2 = pygame.Rect(bote2PosX, bote2PosY, size, size)


walls = []  # Paredes
player = Player((playerPosX, playerPosY))  # Crear jugador
caja = Caja()
vacios = []
bote = Bote()

level = [
    "WWWWWWWWWWWWWWWWWW",
    "W                W",
    "W                W",
    "W                W",
    "W                W",
    "W                W",
    "W                W",
    "W                W",
    "W                W",
    "W                W",
    "W                W",
    "W                W",
    "W                W",
    "W                W",
    "W                W",
    "W                W",
    "W                W",
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


def colision(dx, dy, especial):
    for wall in walls:
        if player.bobby.colliderect(wall.rect):
            if dx > 0:  # Moving right; Hit the left side of the wall
                MoverCaja(caja.caja1, caja.caja1HitBox, especial, wall, 1)
                MoverCaja(caja.caja2, caja.caja2HitBox, especial, wall, 1)
                MoverCaja(caja.caja3, caja.caja3HitBox, especial, wall, 1)
                player.bobby.right = wall.rect.left
            if dx < 0:  # Moving left; Hit the right side of the wall
                MoverCaja(caja.caja1, caja.caja1HitBox, especial, wall, 2)
                MoverCaja(caja.caja2, caja.caja2HitBox, especial, wall, 2)
                MoverCaja(caja.caja3, caja.caja3HitBox, especial, wall, 2)
                player.bobby.left = wall.rect.right
            if dy > 0:  # Moving down; Hit the top side of the wall
                MoverCaja(caja.caja1, caja.caja1HitBox, especial, wall, 3)
                MoverCaja(caja.caja2, caja.caja2HitBox, especial, wall, 3)
                MoverCaja(caja.caja3, caja.caja3HitBox, especial, wall, 3)
                player.bobby.bottom = wall.rect.top
            if dy < 0:  # Moving up; Hit the bottom side of the wall
                MoverCaja(caja.caja1, caja.caja1HitBox, especial, wall, 4)
                MoverCaja(caja.caja2, caja.caja2HitBox, especial, wall, 4)
                MoverCaja(caja.caja3, caja.caja3HitBox, especial, wall, 4)
                player.bobby.top = wall.rect.bottom
        if caja.caja1.colliderect(wall.rect):
            if dx > 0:  # No dejar pasar la caja desde izquierda
                caja.caja1.right = wall.rect.left
                player.bobby.right = caja.caja1.left
            if dx < 0:  # # No dejar pasar la caja desde derecha
                caja.caja1.left = wall.rect.right
                player.bobby.left = caja.caja1.right
            if dy > 0:  # No dejar pasar la caja desde arriba
                caja.caja1.bottom = wall.rect.top
                player.bobby.bottom = caja.caja1.top
            if dy < 0:  # No dejar pasar la caja desde abajo
                caja.caja1.top = wall.rect.bottom
                player.bobby.top = caja.caja1.bottom
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
        if caja.caja3.colliderect(wall.rect):
            if dx > 0:  # No dejar pasar la caja desde izquierda
                caja.caja3.x -= speed
                player.bobby.x -= speed
            if dx < 0:  # # No dejar pasar la caja desde derecha
                caja.caja3.x += speed
                player.bobby.x += speed
            if dy > 0:  # No dejar pasar la caja desde arriba
                caja.caja3.y -= speed
                player.bobby.y -= speed
            if dy < 0:  # No dejar pasar la caja desde abajo
                caja.caja3.y += speed
                player.bobby.y += speed
        else:
            if especial: # Mover cajas y que no choquen
                if player.bobby.colliderect(caja.caja1):
                    if dx > 0 or dx < 0:
                        caja.caja1.x += dx
                    if dy > 0 or dy < 0:
                        caja.caja1.y += dy
                    # Entre la caja por un lado
                    if caja.caja1.colliderect(caja.caja2):
                        ChecarColision(caja.caja1, caja.caja2, player.bobby)
                    elif caja.caja1.colliderect(caja.caja3):
                        ChecarColision(caja.caja1, caja.caja3, player.bobby)
                elif player.bobby.colliderect(caja.caja2):
                    if dx > 0 or dx < 0:
                        caja.caja2.x += dx
                    if dy > 0 or dy < 0:
                        caja.caja2.y += dy
                    # Entre la caja por un lado
                    if caja.caja2.colliderect(caja.caja1):
                        ChecarColision(caja.caja2, caja.caja1, player.bobby)
                    elif caja.caja2.colliderect(caja.caja3):
                        ChecarColision(caja.caja2, caja.caja3, player.bobby)
                elif player.bobby.colliderect(caja.caja3):
                    if dx > 0 or dx < 0:
                        caja.caja3.x += dx
                    if dy > 0 or dy < 0:
                        caja.caja3.y += dy
                    # Entre la caja por un lado
                    if caja.caja3.colliderect(caja.caja1):
                        ChecarColision(caja.caja3, caja.caja1, player.bobby)
                    elif caja.caja3.colliderect(caja.caja2):
                        ChecarColision(caja.caja3, caja.caja2, player.bobby)
                if player.bobby.colliderect(caja.caja1HitBox): # Jugador jalando caja1
                    if dx < 0 and player.bobby.right <= caja.caja1.left and player.bobby.top < caja.caja1.bottom and player.bobby.bottom > caja.caja1.top:
                        caja.caja1.left = player.bobby.right
                    elif dx > 0 and player.bobby.left >= caja.caja1.right and player.bobby.top < caja.caja1.bottom and player.bobby.bottom > caja.caja1.top:
                        caja.caja1.right = player.bobby.left
                    elif dy < 0 and player.bobby.bottom <= caja.caja1.top and player.bobby.left < caja.caja1.right and player.bobby.right > caja.caja1.left:
                        caja.caja1.top = player.bobby.bottom
                    elif dy > 0 and player.bobby.top >= caja.caja1.bottom and player.bobby.left < caja.caja1.right and player.bobby.right > caja.caja1.left:
                        caja.caja1.bottom = player.bobby.top
                elif player.bobby.colliderect(caja.caja2HitBox): # Jugador jalando caja2
                    if dx < 0 and player.bobby.right <= caja.caja2.left and player.bobby.top < caja.caja2.bottom and player.bobby.bottom > caja.caja2.top:
                        caja.caja2.left = player.bobby.right
                    elif dx > 0 and player.bobby.left >= caja.caja2.right and player.bobby.top < caja.caja2.bottom and player.bobby.bottom > caja.caja2.top:
                        caja.caja2.right = player.bobby.left
                    elif dy < 0 and player.bobby.bottom <= caja.caja2.top and player.bobby.left < caja.caja2.right and player.bobby.right > caja.caja2.left:
                        caja.caja2.top = player.bobby.bottom
                    elif dy > 0 and player.bobby.top >= caja.caja2.bottom and player.bobby.left < caja.caja2.right and player.bobby.right > caja.caja2.left:
                        caja.caja2.bottom = player.bobby.top
                elif player.bobby.colliderect(caja.caja3HitBox): # Jugador jalando caja3
                    if dx < 0 and player.bobby.right <= caja.caja3.left and player.bobby.top < caja.caja3.bottom and player.bobby.bottom > caja.caja3.top:
                        caja.caja3.left = player.bobby.right
                    elif dx > 0 and player.bobby.left >= caja.caja3.right and player.bobby.top < caja.caja3.bottom and player.bobby.bottom > caja.caja3.top:
                        caja.caja3.right = player.bobby.left
                    elif dy < 0 and player.bobby.bottom <= caja.caja3.top and player.bobby.left < caja.caja3.right and player.bobby.right > caja.caja3.left:
                        caja.caja3.top = player.bobby.bottom
                    elif dy > 0 and player.bobby.top >= caja.caja3.bottom and player.bobby.left < caja.caja3.right and player.bobby.right > caja.caja3.left:
                        caja.caja3.bottom = player.bobby.top

            else: # Que no deje pasar a Bobby hacia una caja si no se presiona Espacio
                if player.bobby.colliderect(caja.caja1):
                    if dx > 0:  # Moving right; Hit the left side of the wall
                        player.bobby.right = caja.caja1.left
                    if dx < 0:  # Moving left; Hit the right side of the wall
                        player.bobby.left = caja.caja1.right
                    if dy > 0:  # Moving down; Hit the top side of the wall
                        player.bobby.bottom = caja.caja1.top
                    if dy < 0:  # Moving up; Hit the bottom side of the wall
                        player.bobby.top = caja.caja1.bottom
                elif player.bobby.colliderect(caja.caja2):
                    if dx > 0:  # Moving right; Hit the left side of the wall
                        player.bobby.right = caja.caja2.left
                    if dx < 0:  # Moving left; Hit the right side of the wall
                        player.bobby.left = caja.caja2.right
                    if dy > 0:  # Moving down; Hit the top side of the wall
                        player.bobby.bottom = caja.caja2.top
                    if dy < 0:  # Moving up; Hit the bottom side of the wall
                        player.bobby.top = caja.caja2.bottom
                elif player.bobby.colliderect(caja.caja3):
                    if dx > 0:  # Moving right; Hit the left side of the wall
                        player.bobby.right = caja.caja3.left
                    if dx < 0:  # Moving left; Hit the right side of the wall
                        player.bobby.left = caja.caja3.right
                    if dy > 0:  # Moving down; Hit the top side of the wall
                        player.bobby.bottom = caja.caja3.top
                    if dy < 0:  # Moving up; Hit the bottom side of the wall
                        player.bobby.top = caja.caja3.bottom


def ChecarColision(obj1, obj2, Player):
    if obj1.y < obj2.y and Player.y + 20 < obj1.y:
        obj1.y -= speed
        Player.y -= speed
    elif obj1.y > obj2.y and Player.y + 20 > obj1.y:
        obj1.y += speed
        Player.y += speed
    elif obj1.x > obj2.x and Player.x + 13.5 > obj1.x:
        obj1.x += speed
        Player.x += speed
    elif obj1.x < obj2.x and Player.x + 13.5 < obj1.x:
        obj1.x -= speed
        Player.x -= speed

def MoverCaja(obj1, obj1HitBox, especial, wall, opcion):
    if player.bobby.colliderect(obj1HitBox) and especial:
        if opcion == 1:
            if player.bobby.left >= obj1.right:
                player.bobby.right = wall.rect.left
                obj1.right = player.bobby.left
        if opcion == 2:
            if player.bobby.right <= obj1.left:
                player.bobby.left = wall.rect.right
                obj1.left = player.bobby.right
        if opcion == 3:
            if player.bobby.top >= obj1.bottom:
                player.bobby.bottom = wall.rect.top
                obj1.bottom = player.bobby.top
        if opcion == 4:
            if player.bobby.bottom <= obj1.top:
                player.bobby.top = wall.rect.bottom
                obj1.top = player.bobby.bottom
