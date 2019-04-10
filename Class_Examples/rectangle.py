import pygame, sys

pygame.init()

funZone = pygame.display.set_mode((400, 400))
posX = 200
posY = 200

pygame.display.set_caption("Funzone :^)")

blue = (0, 0, 255)
red = (255, 0, 0)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                posX += 10
            elif event.key == pygame.K_a:
                posX -= 10


    funZone.fill(blue)
    pygame.draw.rect(funZone, red, (posX, posY, 100, 100), 0)
    pygame.display.update()


    