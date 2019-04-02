# Pygame Visuals - Screen, Colors, Shapes, and Images

Now that we are more familiar with the basics, we can start to incorporate more artistic objects and functionalities into our pygame program. We will breakdown this lesson into four categories:
- Screen Dimensions
- Colors
- Drawing Lines and Shapes
- Importing and Setting Images


## Screen Dimensions
It is important to understand the x-y coordinate system that is used to reference pixel locations in pygame. We are all familiar with the classic x-y plane you were taught in algebra class. 

![x-y plane](

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


Here is how we set the background color \
let `screen = pygame.display.set_mode(())`, then `screen.fill(r, g, b)` will fill up the entire screen with a color




## drawing


This is pseudo-code (give you a general idea) but will also provide an example:


### drawing lines
`pygame.draw.lines(screen, color, closed, coordinates, thickness)`


example: `pygame.draw.lines(screen, black, False, [(100,100), (150,200), (200,100)], 1)`


## drawing rectangles
`pygame.draw.rect(screen, color, (x,y,width,height), thickness)`


## drawing circles
`pygame.draw.circle(screen, color, (x,y), radius, thickness)

