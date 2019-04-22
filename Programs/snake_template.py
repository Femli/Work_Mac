import pygame, sys
from pygame.locals import*

pygame.init()

width = 500
height = 500
screen = pygame.display.set_mode((width, height))

img = pygame.image.load('Images/sponge.jpg')
img = pygame.transform.scale(img, (30, 30))
count = 5

posX = 255
posY = 255

moveUp = False
moveDown = False
moveLeft = False
moveRight = False

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                moveUp = True
                moveDown = False
                moveLeft = False
                moveRight = False
            if event.key == pygame.K_s:
                moveDown = True
                moveUp = False
                moveLeft = False
                moveRight = False
            if event.key == pygame.K_a:
                moveLeft = True
                moveRight = False
                moveUp = False
                moveDown = False
            if event.key == pygame.K_d:
                moveRight = True
                moveLeft = False
                moveUp = False
                moveDown = False

    if moveUp and posY >= 0:
        posY -= count
    elif moveDown and posY <= 500 - 30:
        posY += count
    elif moveLeft and posX >= 0:
        posX -= count
    elif moveRight and posX <= 500 - 30:
        posX += count

    screen.fill((255, 255, 255))
    screen.blit(img, (posX, posY))
    pygame.display.update()
'''
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        posY -= count
    if keys[pygame.K_s]:
        posY += count
    if keys[pygame.K_a]:
        posX -= count
    if keys[pygame.K_d]:
        posX += count
'''

