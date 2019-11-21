import pygame, os, level1, menu
from pygame.locals import *

# Inicializar pygame ---
os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()
# Posicionar pantalla
pygame.display.set_caption("Push Planet")
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
BackGround = level1.Background([0, 0])
font = pygame.font.Font('freesansbold.ttf', 18)
# Colores
color1 = [(255, 100, 0),(255, 100, 100),0]
color2 = [(50, 255, 0),(255, 100, 100),0]
color3 = [(50, 0, 0),(0, 100, 100),0]
# Ciclo
running = True
menus = True
# Metodos
#Pause
def Pause():
    pause = True
    option = 0
    while pause:
        clock.tick(30)
        screen.blit(menu.BackGround.image, BackGround.rect)
        screen.blit(menu.continuar, (540, 310))
        screen.blit(menu.restart, (540, 430))
        screen.blit(menu.exit, (540, 550))
        screen.blit(menu.pausa, (474, 100))
        if option == 0:
            menu.Bordes(screen, [540, 310])
        if option == 1:
            menu.Bordes(screen, [540, 430])
        if option == 2:
            menu.Bordes(screen, [540, 550])
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                return False
            if e.type == pygame.KEYUP and e.key == pygame.K_UP:
                option = menu.Ciclo2(option)
            if e.type == pygame.KEYUP and e.key == pygame.K_DOWN:
                option = menu.Ciclo1(option)
            if e.type == pygame.KEYDOWN and (e.key == pygame.K_SPACE or e.key == pygame.K_RETURN):
                if option == 0:
                    return True
                if option == 1:
                    level1.restart()
                    return True
                if option == 2:
                    return False
        pygame.display.flip()
#Teclado
def Teclado(nivel):
    global running
    for e in pygame.event.get():
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            nivel = Pause()
        if e.type == pygame.QUIT:
            nivel = Pause()
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        if key[pygame.K_SPACE]:
            especial = True
        else:
            especial = False
        level1.player.move("left", especial)
    elif key[pygame.K_RIGHT]:
        if key[pygame.K_SPACE]:
            especial = True
        else:
            especial = False
        level1.player.move("right", especial)
    elif key[pygame.K_UP]:
        if key[pygame.K_SPACE]:
            especial = True
        else:
            especial = False
        level1.player.move("up", especial)
    elif key[pygame.K_DOWN]:
        if key[pygame.K_SPACE]:
            especial = True
        else:
            especial = False
        level1.player.move("down", especial)
    if key[pygame.K_PAGEDOWN]:
        print "Player BOTTOM: ", level1.player.bobby.bottom, "Caja TOP: ", level1.caja.caja1.top
        print "Player TOP: ", level1.player.bobby.top, "Caja BOTOOM: ", level1.caja.caja1.bottom
        print "Player LEFT: ", level1.player.bobby.left, "Caja RIGHT: ", level1.caja.caja1.right
        print "Player RIGHT: ", level1.player.bobby.right, "Caja LEFT: ", level1.caja.caja1.left
    return nivel
#Menu principal
def MainMenu():
    running = True
    option = 0
    while running:
        clock.tick(30)
        screen.blit(menu.BackGround.image, BackGround.rect)
        screen.blit(menu.play, (540, 310))
        screen.blit(menu.options, (540, 430))
        screen.blit(menu.exit, (540, 550))
        screen.blit(menu.logo, (459, 100))
        if option == 0:
            menu.Bordes(screen, [540, 310])
        if option == 1:
            menu.Bordes(screen, [540, 430])
        if option == 2:
            menu.Bordes(screen, [540, 550])
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            if e.type == pygame.KEYUP and e.key == pygame.K_UP:
                option = menu.Ciclo2(option)
            if e.type == pygame.KEYUP and e.key == pygame.K_DOWN:
                option = menu.Ciclo1(option)
            if e.type == pygame.KEYDOWN and (e.key == pygame.K_SPACE or e.key == pygame.K_RETURN):
                if option == 0:
                    LevelSelector()
                if option == 2:
                    running = False
        pygame.display.flip()
#Seleccionar nivel
def LevelSelector():
    selector = True
    option = 0
    while selector:
        clock.tick(30)
        screen.blit(menu.BackGround.image, BackGround.rect)
        screen.blit(menu.logo, (459, 100))
        screen.blit(menu.level1, (230, 310))
        screen.blit(menu.level2, (515, 310))
        screen.blit(menu.level3, (800, 310))
        if option == 0:
            menu.Bordes2(screen, [230, 310])
        if option == 1:
            menu.Bordes2(screen, [515, 310])
        if option == 2:
            menu.Bordes2(screen, [800, 310])
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                selector = False
            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                selector = False
            if e.type == pygame.KEYUP and e.key == pygame.K_LEFT:
                option = menu.Ciclo2(option)
            if e.type == pygame.KEYUP and e.key == pygame.K_RIGHT:
                option = menu.Ciclo1(option)
            if e.type == pygame.KEYDOWN and (e.key == pygame.K_SPACE or e.key == pygame.K_RETURN):
                if option == 0:
                    selector = False
                    Level1()
                if option == 2:
                    running = False
        pygame.display.flip()

def Level1():
    level1.restart()
    level = True
    while level:
        dt = clock.tick(100)
        # print "Caja", level1.caja.caja1.x
        # print "Personaje", level1.player.bobby.x
        level = Teclado(level)
        if not level:
            return
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
            level1.restart()
        # pygame.draw.rect(screen, (100, 100, 100), level1.player.bobby)
        pygame.draw.rect(screen, (255, 50, 0), level1.bote.bote1)
        pygame.draw.rect(screen, (100, 255, 0), level1.bote.bote2)
        pygame.draw.rect(screen, color1[color1[2]], level1.caja.caja1)
        pygame.draw.rect(screen, color2[color2[2]], level1.caja.caja2)
        pygame.draw.rect(screen, color3[color3[2]], level1.caja.caja3)
        screen.blit(level1.player.image, (level1.player.bobby.x-6, level1.player.bobby.y))
        pygame.display.flip()

# Main
MainMenu()
