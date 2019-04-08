## THIS IS A BASIC PROGRAM TEMPLATE THAT CLOSES THE PROGRAM WHEN WE PRESS THE TOP LEFT X BUTTON ##

import pygame

pygame.init()

screenWidth = 400
screenHeight = 500

screen = pygame.display.set_mode((screenWidth, screenHeight))

gameOff = False

While not gameOff:
  
  for event in pygame.event.get():
    
    if event.type() == pygame.QUIT:
      gameOff = True
      pygame.quit()
      
  
