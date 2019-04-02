# Introduction to Pygame

Now that we have completed all the pre-requisites for pygame, you should all be EXPERTS at python :^) \
We can now move on to pygame stuff.

At first, all this information may seem overwhelming, but rest assured that indeed it really is overwhelming :D

No but seriously, it might get tough but don't give up! We are almost done

## Major python components

`import` is a statement that tells python to import a module (from the many that exist in our local library)
`import pygame` in this case, we want to import the pygame module that will give us access to a loooot of tools
`import sys` allows us to hard-quit python by closing the pygame display screen

`pygame` Is a module that contains various classes for creating a game
`pygame.init()` The most important pygame method: allows us to start the pygame program
`pygame.display.set_mode(())` This is where we set the size of our game screen window
`pygame.display.update()` Need to run this to update screen content, everytime code iterates -- this concept is known as 'double buffering' which enables us to update the game every single frame
`while (True): # do something` is the infinite loop that is required to run the game

Here is how we set the background color9
let `screen = pygame.display.set_mode(())`, then `screen.fill(r, g, b)` will fill up the entire screen with a color


```
for event in pygame.event.get():
        if event.type == pygame.QUIT:
             pygame.quit(); sys.exit();
```
This is the most basic pygame app we can run. It simply creates the display and allows us to exit
`pygame.event.get()` collects all the events that the program records since `pygame.init()` is ran
each iteration of the for-loop, the variable event will collect the events happening in the pygame program
The if-else statement is there to let us know when the event of pressing the close window
`pygame.quit()` will close down the python application
`sys.exit()` will shut down the infinite loop, effectively killing the entire app
    

## Screen dimensions
Based on set dimensions, let's say in this case 400 x 800, then:

Upper left: (0, 0)
Upper right : (400, 0)
Lower left: (0, 800)
Lower right: (400, 800)

X coordinate increases from left to right
y coordinate increases from top to bottom

## colors
colors will be composed of a tupule with three numbers: (r, b, g)
where r is red from a range of 0 to 255, g is green from a range of 0 to 255, and b is blue from a range of 0 to 255

```
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
black = (0,0,0)
```
0 - 255 is a range of color shading, where:
0 is the brightest
255 is the darkest


## drawing

This is pseudo-code (give you a general idea) but will also provide an example:

### drawing lines
`pygame.draw.lines(screen, color, closed, coordinates, thickness)`

example: `pygame.draw.lines(screen, black, False, [(100,100), (150,200), (200,100)], 1)`

## drawing rectangles
`pygame.draw.rect(screen, color, (x,y,width,height), thickness)`

## drawing circles
`pygame.draw.circle(screen, color, (x,y), radius, thickness)



