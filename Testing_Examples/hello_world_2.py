import pygame

pygame.init()

clock = pygame.time.Clock()

displayWidth = 800
displayHeight = 500
gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption("Pepe")

#COLORS
black = (0, 0, 0)
white = (255, 255, 255)
toadImage = pygame.image.load("toad.jpg")

gameOn = True

def carSprite(x, y): 
    gameDisplay.blit(toadImage, (x, y))

xPos = displayWidth * .5
yPos = displayHeight * .8

while gameOn:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameON = False

    gameDisplay.fill(black) #CHANGE THE BACKGROUND COLOR
    carSprite(xPos, yPos)

    pygame.display.update() 
    clock.tick(60)

pygame.quit()
quit()


    