import pygame, sys, random
from pygame.locals import*

#grapes...get some
class ball:

    def __init__(self, X, Y, radius):
        self.x = X
        self.y = Y
        self.rad = radius

class direction:

    def __init__(self):
        self.up = False
        self.down = False
        self.left = False
        self.right = False

    def start(self):
        x = random.randint(0, 10)
        if x > 5:
            self.right = True
        else:
            self.left = True

class platform:

    def __init__(self, topX, topY, width, height):
        self.x = topX
        self.y = topY
        self.width = width
        self.height = height


pygame.init()

screenW = 600
screenH = 500
screen = pygame.display.set_mode((screenW, screenH))

FPS = 60
clock = pygame.time.Clock()

posY = 200
posX = 50


ballX = 300
ballY = 250
radius = 10

moveLeft = False
moveRight = True
moveUp = False
moveDown = False

leftP = platform(200, 50, 20, 100)
#rightP = platform(posX, posY, 20, 100)
ball = ball(ballX, ballY, radius)
move = direction()


def collision(plat, ball, move):
    if move.left and any(plat.x < y < (plat.x + plat.height) for y in range(ball.y - ball.rad, ball.y + ball.rad)) and (ball.x - ball.rad) == (ball.x + plat.width):
        move.left = False
        move.right = True
        if any(plat.y <= y <= (plat.y + plat.hieght / 2) for y in range(ball.y - ball.rad, ball.y + ball.rad)):
            move.down = True
            move.up = False
        #elif any((posY + 50) < y <= (posY + 100 ) for y in range(ballY - radius, ballY + radius)):
        else:
            move.up = True
            move.down = False

while True:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and posY > 0:
        posY -= 3
    if keys[pygame.K_s] and posY < 400:
        posY += 3

    screen.fill((0, 0, 0))

    ### BALL MOVING LEFT AND RIGHT
    if ballX < (screenW - radius) and moveRight:
        ballX += 5
        if ballX >= (screenW - radius):
            moveRight = False
            moveLeft = True
    elif ballX > radius and moveLeft:
        ballX -= 5
    else:
        moveRight = True
        moveLeft = False

    #move.start()
    #collision(leftP, ball, move)
    #if moveLeft and posY <= ballY <= (posY + 100) and (ballX - radius) == (posX + 20):

    ### LEFT PLATFORM COLLISION - THE FRONT
    if moveLeft and any(posY < y < (posY + 100) for y in range(ballY - radius, ballY + radius)) and (ballX - radius) == (posX + 20):
        moveLeft = False
        moveRight = True
        if any(posY <= y <= (posY + 50) for y in range(ballY - radius, ballY + radius)):
            moveDown = True
            moveUp = False
        else:
            moveUp = True
            moveDown = False

    ### EXIT THE GAME
    #if moveLeft and (ballX - radius) <= 0:
    #    pygame.quit(); sys.exit()

    ### LEFT PLATFORM COLLISION - TOP AND BOTTOM
    if moveLeft and posX <= ballX < (posX + 20) and (ballY-radius) == (posY+100) or (ballY+radius) == posY:
        if (ballY-radius) == (posY + 100):
            moveDown = True
            moveUp = False
        if (ballY+radius) == posY:
            moveDown = False
            moveUp = True

    ### BALL BOUNCING UP AND DOWN
    if moveUp and (ballY + radius) < screenH:
        ballY += 5
    else:
        moveUp = False
        moveDown = True
    if moveDown and (ballY - radius) > 0:
        ballY -= 5
    else:
        moveUp = True
        moveDown = False

    pygame.draw.rect(screen, (255, 255, 255), (posX, posY, 20, 100), 0)
    #pygame.draw.rect(screen, (255, 255, 255), (leftP.x, leftP.y, leftP.width, leftP.height), 0)
    pygame.draw.circle(screen, (255, 0, 0), (ballX, ballY), radius, 0)
    #pygame.draw.circle(screen, (255, 0, 0), (ball.x, ball.y), ball.rad, 0)
    print("({}, {})".format(ballX, ballY))

    pygame.display.update()