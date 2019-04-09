import pygame
import sys

pygame.init()

box = pygame.display.set_mode((400, 400))
yellow = (255, 255, 0)
black = (0, 0, 0)
green = (0, 255, 00)
blue = (0, 0, 255)
red = (255, 0, 0)

color = black
while True:

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() 
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                color = red
            elif event.key == pygame.K_a:
                color = green
            elif event.key == pygame.K_d:
                color = blue
    
    box.fill((color))
    pygame.display.update()
'''
    pygame.draw.lines(box, black, False, [ (0, 200), (400, 200)], 5 )
    pygame.draw.rect(box, blue, (100, 200, 200, 50), 5)
    pygame.draw.circle(box, red, (200, 200), 100, 5 )
'''
    



