import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((100,200))


while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.quit()
            break
        
    screen.fill((150, 50, 200))
    pygame.display.update()


