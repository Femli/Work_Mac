#Basic Pygame Syntax 

Now that we have Pip and Pygame installed it is time to get familiar with pygame. 
Pygame can be very simple if you already know basic Python code. 

Pygame is one the best library games to create basic 2D retro arcade games like **Pac Man**, **Space Invaders**, and **Tetris** 
Before we get started lets look at a Basic Pygame Application and find the similarities

'''
import pygame
pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False 

while not done:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True
      
  pygame.display.flip()
'''
