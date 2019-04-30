import pygame, sys
from pygame.locals import*

pygame.init()

screenW = 600
screenH = 500
screen = pygame.display.set_mode((screenW, screenH))

FPS = 60
clock = pygame.time.Clock()

posY = 200
posY2 = 200

ballX = 300
ballY = 250

moveLeft = False
moveRight = True
while True:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and posY > 0:
        posY -= 5
    if keys[pygame.K_s] and posY < 400:
        posY += 5
    if keys[pygame.K_UP] and posY2 > 0:
        posY2 -= 5
    if keys[pygame.K_DOWN] and posY2 < 400:
        posY2 += 5

    screen.fill((0, 0, 0))

    if ballX < (screenW - 10) and moveRight:
        ballX += 5
        if ballX >= 520:
            moveRight = False
            moveLeft = True
    if ballX > 10 and moveLeft:
        ballX -= 5
    else:
        moveRight = True
        moveLeft = False
    
    

    pygame.draw.rect(screen, (255, 255, 255), (50, posY, 20, 100), 0)
    pygame.draw.rect(screen, (255, 255, 255), (530, posY2, 20, 100), 0)
    pygame.draw.circle(screen, (255, 0, 0), (ballX, ballY), 10, 0)

    pygame.display.update()

