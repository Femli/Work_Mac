import pygame

pygame.init()

screenWidth = 300
screenHeight = 400
screen = pygame.display.set_mode((screenWidth, screenHeight))

gameOff = False

while not gameOff:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOff = True
            pygame.quit()
    
    screen.fill((255, 0, 0))
    pygame.draw.lines(screen, (0, 0, 0), False, [(100, 100), (200, 200)], 5)
    pygame.draw.rect(screen, (0, 255, 0), (150, 150, 150, 150), 5)
    pygame.draw.circle(screen, (0, 0, 255), (50, 50), 50, 5)
    pygame.display.update()

    

'''
    for x in range(1,4):
        pygame.draw.lines(screen, (255, 0, 0), False, [(10*x, 0), (x*100, x*100)], 4)

    for x in range(1, 6):
        pygame.draw.lines(screen, (0, 0, 255), False, [(30*x, 0), (x*100, x*100)], 4)

    pygame.draw.lines(screen, (0, 255, 0), False, [(0, 0), (100, 100)], 4)

    pygame.draw.rect(screen, (0, 0, 255), (300, 300, 100, 100), 2)
    pygame.draw.rect(screen, (0, 0, 255), (300, 300, 200, 200), 2)

    pygame.draw.circle(screen, (255, 0, 0), (300, 300), 70, 2)
'''
    

    



    
