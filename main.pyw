import pygame, os
import sys
sys.path.insert(1, 'source/')
import level1, menu, hud, time, level2, level3
from pygame.locals import *
from random import randint

# Inicializar pygame ---
os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()
# Posicionar pantalla
pygame.display.set_caption("Push Planet")
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 18)
# Colores

# Ciclo
running = True
menus = True
vol = 0.2
# Metodos

#Pause
def Pause(n):
    BackGround = menu.Background((0,0))
    pause = True
    option = 0
    while pause:
        clock.tick(30)
        screen.blit(menu.BackGround.image, BackGround.rect)
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
                    if n == 0:
                        level1.restart()
                    if n == 1:
                        level2.restart()
                    if n == 2:
                        level3.restart()
                    return True
                if option == 2:
                    return False
        pygame.display.flip()

def Muerte(n):
    pause = True
    option = 0
    while pause:
        clock.tick(30)
        screen.blit(menu.bg_death, (0, 0))
        screen.blit(menu.restart, (540, 430))
        screen.blit(menu.exit, (540, 550))
        screen.blit(menu.gameover, (357, 250))
        if option == 0:
            option = 1
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
                if option == 1:
                    if n == 0:
                        level1.restart()
                    if n == 1:
                        level2.restart()
                    if n == 2:
                        level3.restart()
                    return True
                if option == 2:
                    return False
        pygame.display.flip()
def Opciones():
    global vol
    pause = True
    option = 1
    while pause:
        pygame.mixer.music.set_volume(vol)
        clock.tick(30)
        screen.blit(menu.BackGround.image, BackGround.rect)
        screen.blit(menu.opciones, (438, 96))
        screen.blit(menu.exit, (540, 550))
        screen.blit(menu.volumen1, (504, 270))
        screen.blit(menu.volumen2, (340, 335))
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
                    if n == 0:
                        level1.restart()
                    if n == 1:
                        level2.restart()
                    if n == 2:
                        level3.restart()
                    return True
                if option == 2:
                    return False
            if option == 1:
                if e.type == pygame.KEYUP and e.key == pygame.K_LEFT and vol >= 0.1:
                    vol -= 0.1
                if e.type == pygame.KEYUP and e.key == pygame.K_RIGHT and vol <= 0.9:
                    vol += 0.1
        if option == 0:
            option = 1
        if option == 1:
            pygame.draw.rect(screen, (12, 17, 118), (342, 337, vol * 596, 46))
        if option == 2:
            pygame.draw.rect(screen, (96, 102, 100), (342, 337, vol * 596, 46))
            menu.Bordes(screen, [540, 550])
        pygame.display.flip()
#Teclado
def Teclado(nivel, n):
    global running
    for e in pygame.event.get():
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            nivel = Pause(n)
        if e.type == pygame.QUIT:
            nivel = Pause(n)
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        if key[pygame.K_SPACE]:
            especial = True
        else:
            especial = False
        if n == 0:
            level1.player.move("left", especial)
        if n == 1:
            level2.player.move("left", especial)
        if n == 2:
            level3.player.move("left", especial)
    elif key[pygame.K_RIGHT]:
        if key[pygame.K_SPACE]:
            especial = True
        else:
            especial = False
        if n == 0:
            level1.player.move("right", especial)
        if n == 1:
            level2.player.move("right", especial)
        if n == 2:
            level3.player.move("right", especial)
    elif key[pygame.K_UP]:
        if key[pygame.K_SPACE]:
            especial = True
        else:
            especial = False
        if n == 0:
            level1.player.move("up", especial)
        if n == 1:
            level2.player.move("up", especial)
        if n == 2:
            level3.player.move("up", especial)
    elif key[pygame.K_DOWN]:
        if key[pygame.K_SPACE]:
            especial = True
        else:
            especial = False
        if n == 0:
            level1.player.move("down", especial)
        if n == 1:
            level2.player.move("down", especial)
        if n == 2:
            level3.player.move("down", especial)
    return nivel
#Menu principal
def MainMenu():
    BackGround = menu.Background((0,0))
    pygame.mixer.music.load("assets/songs/menu.mp3")
    pygame.mixer.music.play()
    running = True
    option = 0
    while running:
        pygame.mixer.music.set_volume(vol)
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
                    LevelSelector(BackGround)
                if option == 1:
                    Opciones()
                if option == 2:
                    running = False
        pygame.display.flip()
#Seleccionar nivel
def LevelSelector(BackGround):
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
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load("assets/songs/menu.mp3")
                    pygame.mixer.music.play()
                if option == 1:
                    selector = False
                    Level2()
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load("assets/songs/menu.mp3")
                    pygame.mixer.music.play()
                if option == 2:
                    selector = False
                    Level3()
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load("assets/songs/menu.mp3")
                    pygame.mixer.music.play()
        pygame.display.flip()
def Aleatorio(level, power, walls):
    for wall in walls:
        if level.choque1:
            level.humo1.terminado = False
            level.caja.caja1.x = randint(320, 680)
            level.caja.caja1.y = randint(354, 680)
            level.humo1.rect.x = level.caja.caja1.x
            level.humo1.rect.y = level.caja.caja1.y
            if level.caja.caja1.colliderect(wall.rect) or level.ColisionEnemigoCaja(level.caja.caja1) or (level.caja.caja1.colliderect(level.caja.caja2) or level.caja.caja1.colliderect(level.caja.caja3)):
                level.choque1 = True
                Aleatorio(level, power, walls)
            else:
                level.choque1 = False
            level.humo2.rect.x = level.caja.caja1.x
            level.humo2.rect.y = level.caja.caja1.y
            level.humo2.terminado = False
        if level.choque2:
            level.humo1.terminado = False
            level.caja.caja1.x = randint(320, 680)
            level.caja.caja1.y = randint(354, 680)
            level.humo1.rect.x = level.caja.caja2.x
            level.humo1.rect.y = level.caja.caja2.y
            if level.caja.caja2.colliderect(wall.rect) or level.ColisionEnemigoCaja(level.caja.caja2) or (level.caja.caja2.colliderect(level.caja.caja1) or level.caja.caja2.colliderect(level.caja.caja3)):
                level.choque2 = True
                Aleatorio(level, power, walls)
            else:
                level.choque2 = False
            level.humo1.rect.x = level.caja.caja2.x
            level.humo1.rect.y = level.caja.caja2.y
            level.humo2.terminado = False
        if level.choque3:
            level.humo1.terminado = False
            level.caja.caja1.x = randint(320, 680)
            level.caja.caja1.y = randint(354, 680)
            level.humo1.rect.x = level.caja.caja3.x
            level.humo1.rect.y = level.caja.caja3.y
            if level.caja.caja3.colliderect(wall.rect) or level.ColisionEnemigoCaja(level.caja.caja3) or (level.caja.caja3.colliderect(level.caja.caja2) or level.caja.caja3.colliderect(level.caja.caja1)):
                level.choque3 = True
                Aleatorio(level, power, walls)
            else:
                level.choque3 = False
            level.humo1.rect.x = level.caja.caja3.x
            level.humo1.rect.y = level.caja.caja3.y
            level.humo2.terminado = False
        if level.caja.caja1.colliderect(level.bote.nave):
            level.humo1.rect.x = level.caja.caja1.x
            level.humo1.rect.y = level.caja.caja1.y
            level.humo1.terminado = False
            level.vida += power
            level.caja.caja1.x = randint(320, 680)
            level.caja.caja1.y = randint(354, 680)
            if level.caja.caja1.colliderect(wall.rect) or level.ColisionEnemigoCaja(level.caja.caja1) or level.caja.caja1.colliderect(level.player.bobby) or (level.caja.caja1.colliderect(level.caja.caja2) or level.caja.caja1.colliderect(level.caja.caja3)):
                level.choque1 = True
                Aleatorio(level, power, walls)
            else:
                level.choque1 = False
            level.humo2.rect.x = level.caja.caja1.x
            level.humo2.rect.y = level.caja.caja1.y
            level.humo2.terminado = False
            level.latas += 1
        if level.caja.caja2.colliderect(level.bote.nave):
            level.humo1.rect.x = level.caja.caja1.x
            level.humo1.rect.y = level.caja.caja1.y
            level.humo1.terminado = False
            level.vida += power
            level.caja.caja2.x = randint(320, 680)
            level.caja.caja2.y = randint(354, 680)
            if level.caja.caja2.colliderect(wall.rect) or level.ColisionEnemigoCaja(level.caja.caja2) or level.caja.caja2.colliderect(level.player.bobby) or (level.caja.caja2.colliderect(level.caja.caja1) or level.caja.caja2.colliderect(level.caja.caja3)):
                level.choque2 = True
                Aleatorio(level, power, walls)
            else:
                level.choque2 = False
            level.humo2.rect.x = level.caja.caja1.x
            level.humo2.rect.y = level.caja.caja1.y
            level.humo2.terminado = False
            level.latas += 1
        if level.caja.caja3.colliderect(level.bote.nave):
            level.humo1.rect.x = level.caja.caja1.x
            level.humo1.rect.y = level.caja.caja1.y
            level.humo1.terminado = False
            level.vida += power
            level.caja.caja3.x = randint(320, 680)
            level.caja.caja3.y = randint(354, 680)
            if level.caja.caja3.colliderect(wall.rect) or level.ColisionEnemigoCaja(level.caja.caja3) or level.caja.caja3.colliderect(level.player.bobby) or (level.caja.caja3.colliderect(level.caja.caja2) or level.caja.caja3.colliderect(level.caja.caja1)):
                level.choque3 = True
                Aleatorio(level, power, walls)
            else:
                level.choque3 = False
            level.humo2.rect.x = level.caja.caja1.x
            level.humo2.rect.y = level.caja.caja1.y
            level.humo2.terminado = False
            level.latas += 1

def Level1():
    BackGround = level1.Background([0, 0])
    pase = False
    destino = (0,0)
    level1.restart()
    power = 400
    level = level1.AnimacionTutorial(screen)
    level1.AnimacionNave(screen)
    level1.AnimacionEnemigo(screen, True)
    t0 = time.time()
    pygame.mixer.music.stop()
    pygame.mixer.music.load("assets/songs/theme.mp3")
    pygame.mixer.music.play()
    while level:
        pygame.mixer.music.set_volume(vol)
        dt = clock.tick(50)
        if level1.vida <= 0:
            level = Muerte(0)
        # print "Caja", level1.caja.caja1.x
        # print "Personaje", level1.player.bobby.x
        level = Teclado(level, 0)
        if not level:
            return
        # Dibujar la escena
        screen.blit(BackGround.image, BackGround.rect)
        screen.blit(level1.vacio, (280, 0))
        for wall in level1.walls:
            screen.blit(level1.imagenWall, (wall.rect.x, wall.rect.y))
        Aleatorio(level1, power, level1.walls)
        screen.blit(level1.bote.image, level1.bote.rect)
        screen.blit(level1.caja.image, level1.caja.caja1)
        screen.blit(level1.caja.image, level1.caja.caja2)
        screen.blit(level1.caja.image, level1.caja.caja3)
        screen.blit(level1.player.image, (level1.player.bobby.x-6, level1.player.bobby.y))
        screen.blit(hud.barra, (0,0))
        screen.blit(hud.vida, (0,0))
        screen.blit(hud.cesto, (650,5))
        screen.blit(hud.igual, (700,0))
        if level1.latas >= 1:
            screen.blit(hud.lata, (760,12))
        if level1.latas >= 2:
            screen.blit(hud.lata, (810,12))
        if level1.latas >= 3:
            screen.blit(hud.lata, (860,12))
        if level1.latas >= 4:
            screen.blit(hud.lata, (910,12))
            level1.cestos += 1
            level1.latas = 0
        screen.blit(hud.palomita, (963,5))
        screen.blit(hud.igual, (1020,0))
        if level1.vida > 586:
            level1.vida = 586
        screen.blit(hud.barra2, (50,5))
        pygame.draw.rect(screen, (255, 0, 21), (52, 7, level1.vida, 36))
        destino = level1.AIEnemigo(destino, screen)
        if level1.cestos >= 1:
            screen.blit(hud.cesto, (1080,5))
        if level1.cestos >= 2:
            screen.blit(hud.cesto, (1130,5))
        if level1.cestos >= 3:
            screen.blit(hud.cesto, (1180,5))
        if level1.cestos >= 4:
            level = False
            screen.blit(hud.cesto, (1230,5))
            level1.AnimacionFinal(screen)
            pase = True
        if not level1.humo1.terminado:
            level1.humo1.animacion(screen)
        if not level1.humo2.terminado:
            level1.humo2.animacion(screen)
        if not level1.humo3.terminado:
            level1.humo3.animacion(screen)
        if not level1.humo4.terminado:
            level1.humo4.animacion(screen)
        pygame.display.flip()
        level1.vida -= 0.5
        if pase:
            Level2()

def Level2():
    BackGround = level2.Background([0, 0])
    pase = False
    destino = (0,0)
    level2.restart()
    power = 400
    level = level2.AnimacionTutorial(screen)
    level2.AnimacionNave(screen)
    t0 = time.time()
    pygame.mixer.music.stop()
    pygame.mixer.music.load("assets/songs/theme.mp3")
    pygame.mixer.music.play()
    level2.cestos = 1
    while level:
        pygame.mixer.music.set_volume(vol)
        dt = clock.tick(50)
        if level2.vida <= 0:
            level = Muerte(1)
        # print "Caja", level2.caja.caja1.x
        # print "Personaje", level2.player.bobby.x
        level = Teclado(level, 1)
        if not level:
            return
        # Dibujar la escena
        screen.fill((255, 255, 255))
        screen.blit(BackGround.image, BackGround.rect)
        screen.blit(level2.vacio, (280, 0))
        for wall in level2.walls:
            screen.blit(level2.imagenWall, (wall.rect.x, wall.rect.y))
        Aleatorio(level2, power, level2.walls)
        screen.blit(level2.bote.image, level2.bote.rect)
        screen.blit(level2.caja.image, level2.caja.caja1)
        screen.blit(level2.caja.image, level2.caja.caja2)
        screen.blit(level2.caja.image, level2.caja.caja3)
        screen.blit(level2.player.image, (level2.player.bobby.x-6, level2.player.bobby.y))
        screen.blit(hud.barra, (0,0))
        screen.blit(hud.vida, (0,0))
        screen.blit(hud.banca, (650,5))
        screen.blit(hud.igual, (700,0))
        if level2.latas >= 1:
            screen.blit(hud.botella, (760,5))
        if level2.latas >= 2:
            screen.blit(hud.botella, (810,5))
        if level2.latas >= 3:
            screen.blit(hud.botella, (860,5))
        if level2.latas >= 4:
            screen.blit(hud.botella, (910,5))
            level2.cestos += 1
            level2.latas = 0
        screen.blit(hud.palomita, (963,5))
        screen.blit(hud.igual, (1020,0))
        screen.blit(hud.barra2, (50,5))
        if level2.vida > 586:
            level2.vida = 586
        pygame.draw.rect(screen, (255, 0, 21), (52, 7, level2.vida, 36))
        destino = level2.AIEnemigo(destino, screen)
        if level2.cestos >= 1:
            screen.blit(hud.banca, (1080,5))
        if level2.cestos >= 2:
            screen.blit(hud.banca, (1130,5))
        if level2.cestos >= 3:
            screen.blit(hud.banca, (1180,5))
        if level2.cestos >= 4:
            level = False
            screen.blit(hud.banca, (1230,5))
            level2.AnimacionFinal(screen)
            pase = True
        if not level2.humo1.terminado:
            level2.humo1.animacion(screen)
        if not level2.humo2.terminado:
            level2.humo2.animacion(screen)
        if not level1.humo3.terminado:
            level1.humo3.animacion(screen)
        if not level1.humo4.terminado:
            level1.humo4.animacion(screen)
        pygame.display.flip()
        level2.vida -= 0.5
    if pase:
        Level3()

def Level3():
    BackGround = level1.Background([0, 0])
    destino = (0,0)
    level3.restart()
    power = 400
    level = level3.AnimacionTutorial(screen)
    level3.AnimacionNave(screen)
    t0 = time.time()
    pygame.mixer.music.stop()
    pygame.mixer.music.load("assets/songs/theme.mp3")
    pygame.mixer.music.play()
    #level3.cestos = 4
    while level:
        pygame.mixer.music.set_volume(vol)
        dt = clock.tick(50)
        if level3.vida <= 0:
            level = Muerte(2)
        # print "Caja", level3.caja.caja1.x
        # print "Personaje", level3.player.bobby.x
        level = Teclado(level, 2)
        if not level:
            return
        # Dibujar la escena
        screen.fill((255, 255, 255))
        screen.blit(BackGround.image, BackGround.rect)
        screen.blit(level3.vacio, (280, 0))
        for wall in level3.walls:
            screen.blit(level3.imagenWall, (wall.rect.x, wall.rect.y))
        Aleatorio(level3, power, level3.walls)
        screen.blit(level3.bote.image, level3.bote.rect)
        screen.blit(level3.caja.image, level3.caja.caja1)
        screen.blit(level3.caja.image, level3.caja.caja2)
        screen.blit(level3.caja.image, level3.caja.caja3)
        screen.blit(level3.player.image, (level3.player.bobby.x-6, level3.player.bobby.y))
        screen.blit(hud.barra, (0,0))
        screen.blit(hud.vida, (0,0))
        screen.blit(hud.cesto, (650,5))
        screen.blit(hud.igual, (700,0))
        if level3.latas >= 1:
            screen.blit(hud.lata, (760,12))
        if level3.latas >= 2:
            screen.blit(hud.lata, (810,12))
        if level3.latas >= 3:
            screen.blit(hud.lata, (860,12))
        if level3.latas >= 4:
            screen.blit(hud.lata, (910,12))
            level3.cestos += 1
            level3.latas = 0
        screen.blit(hud.palomita, (963,5))
        screen.blit(hud.igual, (1020,0))
        screen.blit(hud.barra2, (50,5))
        if level3.vida > 586:
            level3.vida = 586
        pygame.draw.rect(screen, (255, 0, 21), (52, 7, level3.vida, 36))
        destino = level3.AIEnemigo(destino, screen)
        if level3.cestos >= 1:
            screen.blit(hud.cesto, (1080,5))
        if level3.cestos >= 2:
            screen.blit(hud.cesto, (1130,5))
        if level3.cestos >= 3:
            screen.blit(hud.cesto, (1180,5))
        if level3.cestos >= 4:
            level = False
            screen.blit(hud.cesto, (1230,5))
            level3.AnimacionFinal(screen)
        if not level3.humo1.terminado:
            level3.humo1.animacion(screen)
        if not level3.humo2.terminado:
            level3.humo2.animacion(screen)
        if not level1.humo3.terminado:
            level1.humo3.animacion(screen)
        if not level1.humo4.terminado:
            level1.humo4.animacion(screen)
        pygame.display.flip()
        level3.vida -= 0.5
# Main
MainMenu()
