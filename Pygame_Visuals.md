# Pygame Visuals - Screen, Colors, Shapes, and Images

Now that we are more familiar with the basics, we can start to incorporate more artistic objects and functionalities into our pygame program. We will breakdown this lesson into four categories:
- Screen Dimensions
- Colors
- Drawing Lines and Shapes
- Importing and Setting Images


## Screen Dimensions
It is important to understand the x-y coordinate system that is used to reference pixel locations in pygame. We are all familiar with the classic x-y plane that was taught in algebra class. This plane is formally known as the "Cartesian Plane".

![x-y plane](https://user-images.githubusercontent.com/22228100/55430651-85f35f80-5543-11e9-9a04-4134b2cdd37e.png)

Pygame uses a slightly different orientation of the Cartesian plane, where the y-axis is inverted and the origin (0,0) starts at the top left.

![pygame_coordinates](https://user-images.githubusercontent.com/22228100/55430650-85f35f80-5543-11e9-94b1-5268c7f6f933.gif)

The range of our x and y coordinates will be determined by us. In the `python.display.set_mode((Width, Height))` our `Width` is the range of our x-axes and `Height` is the range of our y-axis. 


Lets say for example we set `Width = 400` and `Height = 700`. Then we will have a display that is a rectangle, where the width is 400 pixels and the height is 800 pixels. 

The corners of our display will be as follows: \
Upper left: (0, 0) \
Upper right : (400, 0) \
Lower left: (0, 800) \
Lower right: (400, 800)

**Always remember this:** \
X coordinate increases from left to right \
y coordinate increases from top to bottom


## Colors
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

