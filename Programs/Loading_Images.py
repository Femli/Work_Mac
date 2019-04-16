## THIS IS A PROGRAM THAT WILL HAVE A BLUE RECTANGLE IN THE CENTER, WITH A RED BACKGROUND ##

#IMPORTING THE PYGAME MODULE
import pygame 
import os #MODULE FOR MODIFYING OS SETTINGS

folder = os.path.dirname(os.path.realpath(__file__)) #THIS IS SO WE GET THE FULL IMAGE PATH OF OUR FILES

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

rectW = 100 #WITH OF OUR RECTANGLE
rectH = 100 #HEIGHT OF OUR RECTANGLE

sponge = pygame.image.load(os.path.join(folder, "sponge.jpeg")) #LOADING AN IMAGE INTO OUR SCREEN
sponge = pygame.transform.scale(sponge, (rectW, rectH)) #THIS IS SO WE CAN SCALE THE IMAGE DOWN TO OUR OBJECT SIZE

#DELAYING OUR PROGRAMING SO THAT ONLY A CERTAIN AMOUNT OF FPS WILL BE DISPLAYED
clock = pygame.time.Clock()
FPS = 60

#CREATING OUR ACTUAL GAME WINDOW DISPLAY; IT IS CALLED 'screen'
screen = pygame.display.set_mode((screenWidth, screenHeight)) 

#THIS IS NECESSARY FOR WHEN WE WANT TO SHUT OFF OUR INFINITE WHILE LOOP
gameOff = False 

# COORDINATE VS COUNT : LINEAR VS NONLINEAR (KEEP IN MIND THE NATURE OF OUR MOVEMENT FUNCTION)
jumpState = False
jumpCount = 20
lowLim = rectY 
highLim = rectY - 100
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
                #if rectY == jumpOrigin: #FOR WHEN WE DON'T WANT TO MULTI JUMP
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
    
    screen.fill((red)) #THIS IS WHERE WE SET THE BACKGROUND COLOR TO RED
    pygame.draw.rect(screen, blue, (rectX, rectY, rectW, rectH), 0) #THIS IS WHERE WE CREATE A RECTANGLE
    screen.blit(sponge, (rectX, rectY))  #THIS IS WHERE WE MAKE SURE OUR IMAGE IS ATTACHED TO AN OBJECT AND MOVES WITH THE OBJECT
    pygame.display.update() #UPDATES EVERYTHING THAT WE HAVE DONE TO OUR SCREEN -- VERY IMPORTANT!
  
