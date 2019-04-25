## THIS IS A PROGRAM THAT WILL HAVE A BLUE RECTANGLE IN THE CENTER, WITH A RED BACKGROUND ##

#IMPORTING THE PYGAME MODULE
import pygame 

#THIS ENSURES THAT THE GAME WILL START
pygame.init() 

#WE WILL CREATE VARIABLES WITH COLOR NAMES SO WE CAN USE THEM LATER ON
blue = (0, 0, 255)
red = (255, 0, 0)

#HOW MANY PIXELS WIDE AND TALL OUR GAME WINDOW IS
screenWidth = 400 
screenHeight = 500 

#X AND Y LOCATIONS OF OUR RECTANGLE. NOTICE THAT IT IS HALF THE DIMENSIONS OF THE SCREEN, SO IT WILL ORIGINATE IN THE CENTER
rectX = screenWidth / 2
rectY = screenHeight / 2

#DELAYING OUR PROGRAMING SO THAT ONLY A CERTAIN AMOUNT OF FPS WILL BE DISPLAYED
clock = pygame.time.Clock()
FPS = 30

#CREATING OUR ACTUAL GAME WINDOW DISPLAY; IT IS CALLED 'screen'
screen = pygame.display.set_mode((screenWidth, screenHeight)) 

#THIS IS NECESSARY FOR WHEN WE WANT TO SHUT OFF OUR INFINITE WHILE LOOP
gameOff = False 

'''
jumpState = False
#jumpOrigin = rectY
#jumpCount = 5
jumpBy = 2
jumpCount = 0
countLimit = 5

upLim = rectY - 50
downLim = rectY + 50
jumpOffset = False
'''

# COORDINATE VS COUNT : LINEAR VS NONLINEAR (KEEP IN MIND THE NATURE OF OUR MOVEMENT FUNCTION)
jumpState = False
jumpCount = 10
#lowLim = rectY 
#highLim = rectY - 100
#domain = range(1,10)
#i = 0
#jumpVel = 2
#jumpOrigin = rectY #FOR WHEN WE DON'T WANT TO MULTI JUMP


#THIS WHILE LOOP WILL REPEAT OVER AND OVER, AND MAKE SURE THAT OUR GAME VISUALS ARE CONSTANTLY UPDATING
while not gameOff: 

    clock.tick(FPS)
  
  #THIS IS NECESSARY TO CAPTURE THE EVENTS THAT ARE HAPPENING IN OUR GAME
    for event in pygame.event.get(): 
    
        #IF THE EVENT IS PRESSING THE 'X' BUTTON IN THE TOP LEFT OF THE SCREEN, THEN CLOSE 
        if event.type == pygame.QUIT: 
            gameOff = True #TURN OFF THE INFINITE WHILE LOOP
            pygame.quit() #SHUT OFF THE PROGRAM

        #IF THIS EVENT DETECTS ANY KEY BEING PRESSED, WE WILL EXECUTE THE PROGRAM BELOW:
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                jumpState = True
    
    keyPress = pygame.key.get_pressed()
    if keyPress[pygame.K_a]: #WE THEN TEST IF THE KEY BEING HELD DOWN IS A OR D
        rectX -= 10 #IF KEY A IS HELD DOWN, MOVE LEFT CONTINOUSLY
    elif keyPress[pygame.K_d]:
        rectX += 10 #IF KEY D IS HELD DOWN, MOVE RIGHT CONTINOUSLY
    
    # NONLINEAR
    if jumpState and jumpCount >= -10:
        sign = 1
        rectY -= (jumpCount * 2) * sign
        jumpCount -= 1
        if jumpCount < 0:
            sign = -1
    else:
        sign = 1
        jumpCount = 10
        jumpState = False
    
    '''
    if jumpState and jumpCount > -20:
        if jumpCount > 0:
            rectY -= 10
        elif jumpCount <= 0:
            rectY += 10
        jumpCount -= 1
    else:
        jumpCount = 20
        jumpState = False
    '''

    '''
    if jumpState:
        rectY -= domain[i] ** 2
        i += 1
        if i < len(domain):
            i = 8
            jumpState = False
    elif not jumpState and i >= 0:
        rectY += domain[i] ** 2
        i -= 1
    '''
    '''
    if jumpState:
        rectY -= 10
        if rectY <= highLim:
            jumpState = False
    if not jumpState and rectY < lowLim :
        rectY += 10
    '''

    '''
    # LINEAR AND CAN DOUBLE JUMP
    if jumpState:
        rectY -= 10
        if rectY <= highLim:
            jumpState = False
    if not jumpState and rectY < lowLim:
        rectY += 10
    '''

    '''
    if jumpState == True and jumpBy > 0:
        rectY -= jumpBy * 2
        jumpBy -= 1
    elif jumpBy <= 0 or jumpState == False:
        rectY += jumpBy * 2
        jumpBy += 1
        jumpCount += 1
    '''
    '''
    if jumpState == True:
        if jumpBy > 0:
            rectY -= jumpBy * 2
            jumpBy -= 1
        elif jump < 
        else:
            jumpState = False
            jumpBy = 10
    elif jumpState == False:
        if jumpBy > 0:
            rectY += jumpBy * 2
            jumpBy -= 1
    '''
    '''
    if jumpState:
        jumpBy -= 1
        if rectY <= upLim:
            jumpState = False
            jumpOffset = True
    elif not jumpState and jumpOffset:
        jumpBy += 1
        if rectY >= downLim:
            jumpOffset = False
    '''
    '''
    if jumpState:
        jumpBy -= jumpCount*2
        jumpCount += 1
        if jumpCount >= countLimit:
            jumpBy = 1
            jumpCount = 0
            jumpState = False
            jumpOffset = True
    elif not jumpState and jumpOffset:
        jumpBy += jumpBy * jumpCount
        jumpCount += 1
        if jumpCount >= countLimit:
            jumpOffset = False
    '''
    
    screen.fill((red)) #THIS IS WHERE WE SET THE BACKGROUND COLOR TO RED
    pygame.draw.rect(screen, blue, (rectX, rectY, 100, 100), 0) #THIS IS WHERE WE CREATE A RECTANGLE
    pygame.display.update()
  
