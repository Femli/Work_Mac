import pygame, sys, array
from pygame.locals import*

#SAO is lit

pygame.init()

screenW = 600
screenH = 500
screen = pygame.display.set_mode((screenW, screenH))

FPS = 60
clock = pygame.time.Clock()

posY = 200
posX = 50


ballX = 300
ballY = 250
radius = 10

moveLeft = False
moveRight = True
moveUp = False
moveDown = False


while True:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and posY > 0:
        posY -= 3
    if keys[pygame.K_s] and posY < 400:
        posY += 3

    screen.fill((0, 0, 0))

    if ballX < (screenW - radius) and moveRight:
        ballX += 5
        if ballX >= (screenW - radius):
            moveRight = False
            moveLeft = True
    elif ballX > radius and moveLeft:
        ballX -= 5
    else:
        moveRight = True
        moveLeft = False

    #if moveLeft and posY <= ballY <= (posY + 100) and (ballX - radius) == (posX + 20):
    if moveLeft and any(posY <= y <= (posY + 100) for y in range(ballY - radius, ballY + radius)) and (ballX - radius) == (posX + 20):
        moveLeft = False
        moveRight = True
        if any(posY <= y <= (posY + 50) for y in range(ballY - radius, ballY + radius)):
            moveDown = True
            moveUp = False
        #elif any((posY + 50) < y <= (posY + 100 ) for y in range(ballY - radius, ballY + radius)):
        else:
            moveUp = True
            moveDown = False

    #if moveUp and not moveDown and (ballY - radius) >= 0:
    if moveUp and not moveDown and (ballY - radius) >= 100:
        ballY += 5
        if (ballY - radius) <= 0:
            moveUp = False
            moveDown = True
    #if moveDown and not moveUp and (ballY + radius) <= screenH:
    if moveDown and not moveUp and (ballY + radius) <= 300:
        ballY -= 5
        if (ballY + radius) >= screenH:
            moveUp = True
            moveDown = False

    pygame.draw.rect(screen, (255, 255, 255), (posX, posY, 20, 100), 0)
    pygame.draw.circle(screen, (255, 0, 0), (ballX, ballY), radius, 0)

    pygame.display.update()

