import pygame
from pygame.locals import*


class screen:

    screen = pygame.display.set_mode((width, height))

    def __init__(self):
        self.width = 500
        self.height = 500

    def setCaption(self, caption):
        pygame.display.set_caption(str(caption))

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

    boundaryX = range(posX, posX + width)
    boundaryY = range(posY, posY + height)


    def __init__(self):
        self.posX = 0
        self.posY = 0
        self.width = 10
        self.height = 10
        self.steps = 10

    def setOrigin(self, posX, posY, width, height):
        self.posX = posX
        self.posY = posY
        self.width = width
        self.height = height
    
    def setBoundary(self, startX, endX, startY, endY)
        self.boundaryX = range(startX, startX + endX)
        self.boundaryY = range(startY, startY + endY)

    def setImage(self, fileName):
        self.img = pygame.image.load(str(fileName))

