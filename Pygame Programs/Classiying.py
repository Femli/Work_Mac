import pygame
from pygame.locals import*

class screen:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
    
    def fill(self, color):
        self.screen.fill((color))


def gamePlay():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()

black = (0, 0, 0)
red = (255, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 255)

def playerMovement(posX, posY, steps):
    
    for event in pygame.event.get():
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
screen = screen(500, 500)
player = playerObject()
player.setImage('Images/sponge.jpg')



while True:
    
    gamePlay()
    playerMovement(player.posX, player.posY, player.steps)

    screen.fill(red)
    screen.screen.blit(player.img, (player.posX, player.posY))

    pygame.draw.rect(screen.screen, white, (250, 250, 100, 100), 0)
    pygame.display.update()
    

    


