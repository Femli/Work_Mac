import pygame
from pygame.locals import*

class screen:
    width = 500
    height = 500
    def __init__(self, width, height):
        self.width = width
        self.height = height
        

def playerMovement(posX, posY, steps):
    
    for events in pygame.events.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                posY -= steps
            if event.key == pygame.K_s:
                posY += steps
            if event.key == pygame.K_a:
                posX -= steps
            if event.key == pygame.K_d:
                posX += steps

class playerObject:

    posX = 0
    posY = 0
    width = 10
    height = 10
    boundaryX = range(posX, posX + width)
    boundaryY = range(posY, posY + height)


    def __init__(self):
        self.steps = 10

    def setOrigin(self, posX, posY, width, height):
        self.posX = posX
        self.posY = posY
        self.width = width
        self.height = height
    
    def setBoundary(self, startX, endX, startY, endY):
        self.boundaryX = range(startX, startX + endX)
        self.boundaryY = range(startY, startY + endY)

    def setImage(self, fileName):
        self.img = pygame.image.load(str(fileName))

pygame.init()
screen = screen()

while True:



