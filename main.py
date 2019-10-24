import pygame, os
from pygame.locals import *
import level1

# Inicializar pygame ---
os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()
# Posicionar pantalla
pygame.display.set_caption("Push Planet")
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
BackGround = level1.Background([0, 0])
# Texto
puntos = 0
limite = 50
font = pygame.font.Font('freesansbold.ttf', 18)
# Colores
color1 = [(255, 100, 0),(255, 100, 100),0]
color2 = [(50, 255, 0),(255, 100, 100),0]
# Ciclo
running = True
# Metodos
def Teclado():
    global puntos, running
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            running = False
            # Move the player if an arrow key is pressed
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        level1.player.move(-level1.speed, 0)
        puntos += 1
    if key[pygame.K_RIGHT]:
        level1.player.move(level1.speed, 0)
        puntos += 1
    if key[pygame.K_UP]:
        level1.player.move(0, -level1.speed)
        puntos += 1
    if key[pygame.K_DOWN]:
        level1.player.move(0, level1.speed)
        puntos += 1
    if key[pygame.K_r]:
        level1.restart()

while running:
    clock.tick(100)
    Teclado()
    # Dibujar la escena
    screen.fill((255, 255, 255))
    screen.blit(BackGround.image, BackGround.rect)
    for wall in level1.walls:
        screen.blit(wall.image, (wall.rect.x, wall.rect.y))
        # pygame.draw.rect(screen, (0, 0, 0), wall.rect)
    for vacio in level1.vacios:
        pygame.draw.rect(screen, (202, 204, 206), vacio.rect)
    #pygame.draw.rect(screen, (255, 0, 0), level1.end_rect)

    # pygame.draw.rect(screen, (255, 255, 255), level1.player.bobby)
    if level1.caja.caja1.colliderect(level1.bote.bote1):
        color1[2] = 1
    if level1.caja.caja2.colliderect(level1.bote.bote2):
        color2[2] = 1
    if level1.caja.caja1.colliderect(level1.bote.bote1) and level1.caja.caja2.colliderect(level1.bote.bote2):
        # screen.blit(font.render("GANASTE", True, (0, 0, 0)), (1280/2, 720/2))
        raise SystemExit, "Ganaste"
    screen.blit(level1.player.image, (level1.player.bobby.x, level1.player.bobby.y))
    pygame.draw.rect(screen, (255, 50, 0), level1.bote.bote1)
    pygame.draw.rect(screen, (100, 255, 0), level1.bote.bote2)
    pygame.draw.rect(screen, color1[color1[2]], level1.caja.caja1)
    pygame.draw.rect(screen, color2[color2[2]], level1.caja.caja2)
    puntosTexto = "Movimientos: " + str(puntos) + " / " + str(limite)
    score = font.render(puntosTexto, True, (0, 0, 0))
    screen.blit(score, (100, 700))
    pygame.display.flip()
