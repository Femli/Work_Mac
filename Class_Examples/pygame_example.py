import pygame, sys

pygame.init()
timeDelay = 0

## SCREEN
screenWidth = 500
screenHeight = 500
screen = pygame.display.set_mode((screenWidth, screenHeight))

## COLORS
black = (0, 0, 0); white = (255, 255, 255); red = (255, 0, 0); green = (0, 255, 0); blue = (0, 0, 255)


## PLAYER 1
domain = 10
ranges = 10

playerX = (screenWidth / 2) - domain
playerY = (screenHeight / 2) - ranges 
playerWidth = domain * 2 
playerHeight = ranges * 2 



while True:
    color = black
    #pygame.time.delay(timeDelay)

    for event in pygame.event.get():
        print(event)

        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit();

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                if timeDelay <= 100:
                    timeDelay += 10
                    color = red

            elif event.key == pygame.K_s:
                if timeDelay >= 0:
                    timeDelay -= 10
                    color = blue

    keyPress = pygame.key.get_pressed()
    if keyPress[pygame.K_d]:
        if playerX < 400:
            playerX += 10
    elif keyPress[pygame.K_a]:
        if playerX > 100:
            playerX -= 10

    screen.fill(color)

    pygame.draw.lines(screen, black, False, [(100, 100), (200, 200), 5])
    pygame.draw.rect(screen, green, (playerX, playerY, playerWidth, playerHeight), 0)

    pygame.display.update()
