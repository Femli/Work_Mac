import pygame, sys
from pygame.locals import*
import random

randX = random.randint(0, 500)
randY = random.randint(0, 600)

pygame.init()

img = pygame.image.load('Images/sponge.jpg')
img = pygame.transform.scale(img, (100, 100))

screen = pygame.display.set_mode((500, 600))

posX = 250
posY = 600

clock = pygame.time.Clock()
FPS = 60
timer = 0

while True:
    
    clock.tick(FPS)
    timer += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        posY -= 10
    elif keys[pygame.K_s]:
        posY += 10
    elif keys[pygame.K_a]:
        posX -= 10
    elif keys[pygame.K_d]:
        posX += 10


    screen.fill((255, 255, 255))
    if timer == 500:
        pygame.draw.rect(screen, (255, 0, 255), (randX, randY, 20, 20), 0)
        timer = 0
    screen.blit(img, (posX, posY))
    pygame.display.update()