import pygame, sys

pygame.init()

screen = pygame.display.set_mode((400, 500))
posX = 400 / 2
posY = 500 / 2



while True:
    
    keyPressed = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
    
    if keyPressed[pygame.K_a]:
        posX -= 10
    elif keyPressed[pygame.K_d]:
        posX += 10

    screen.fill((150, 255, 0))

    pygame.draw.rect(screen, (200, 0, 255), (int(posX), int(posY), 20, 10), 0)
    pygame.draw.circle(screen, (255, 0, 0), (200, 200), 100, 5 )

    pygame.display.update()
            
