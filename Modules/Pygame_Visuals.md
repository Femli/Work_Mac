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


Lets say for example we set `Width = 300` and `Height = 400`. Then we will have a display that is a rectangle, where the width is 300 pixels and the height is 400 pixels. 

![Window](https://user-images.githubusercontent.com/22228100/55431959-8f31fb80-5546-11e9-8c7f-3d24d7c361cb.PNG)

The corners of our display will be as follows: \
Upper left: (0, 0) \
Upper right : (300, 0) \
Lower left: (0, 400) \
Lower right: (300, 400)

**Always remember this:** \
X coordinate increases from left to right \
y coordinate increases from top to bottom


## Colors
Colors will be composed of a tupule of three numbers: `(r, b, g)` \
where `r` is red from a range of 0 to 255, `g` is green from a range of 0 to 255, and `b` is blue from a range of 0 to 255. \
0 to 255 is a range of color shading, where 0 is the darkest and 255 is the lightes.

We can isolate the purest colors of red, green and blue with the following: 
```
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
```

We can also mix colors by adjusting different ranges: 
```
yellow = (255, 255, 0)
turquoise = (0, 255, 255)
pink = (255, 0, 255)
white = (255,255,255)
black = (0,0,0)
```


If we want to set the background color of our pygame window, we can do so like this: \
let `screen = pygame.display.set_mode((Width, Height))`, \
then `screen.fill(50, 100, 150)` will fill up the entire screen like this:

![Window2](https://user-images.githubusercontent.com/22228100/55432750-8a6e4700-5548-11e9-9a54-135bd8c06951.PNG)


## Drawing
There are several ways to draw in pygame, and some of the options are pretty complicated. We will only go over how to draw lines, rectangles and circles for now. 

### Lines
The basic syntax for drawing lines is the following: \
`pygame.draw.lines(screen, color, closed, coordinates, thickness)`

`screen` refers to the name we gave to the object that captures `pygame.display.set_mode((Width, Height))` \
`color` refers to the `(r, g, b)` tupule
`closed` refers to the condition of connecting the end-point of our shape/line back to our starting-point. It's either `True` or `False` \
`coordinates` referes to a list object that contains the coordinates that we want to connect with lines, within our display.
`thickness` refers to the actual thickness of our line or shape

Here is an example of how we would use this: \
`pygame.draw.lines(screen, black, False, [(100,100), (200, 200)], 5)`

If done on an a screen with `Width = 300` and `Height = 400`, with a background color of `(255, 0, 0)` (red), we would get the following:

![Window3](https://user-images.githubusercontent.com/22228100/55433797-f81b7280-554a-11e9-99d2-8a324c681ca2.PNG)


### Rectangles
Rectangles follow very similar syntax to lines: \
`pygame.draw.rect(screen, color, (x,y,width,height), thickness)`

In the `(x, y, width, height)` argument, `x` and `y` is the location where we want our rectangle to be positioned. `width` and `height` referes to the actual dimensions of our rectangle.

If we ran the following: `pygame.draw.rect(screen, (0, 255, 0), (150, 150, 150, 150), 5)` we would get: 

![Window4](https://user-images.githubusercontent.com/22228100/55434312-2ea5bd00-554c-11e9-988a-8c8290632c1b.PNG)

Notice that at the coordinates (150, 150) the rectangle extends 150 pixel to the right, and then drops 150 pixels down. It goes back to the rule: **X coordinate increases from left to right and y coordinate increases from top to bottom**



### Circles
Also like rectangles, we have very similar syntax to rectangles: 
`pygame.draw.circle(screen, color, (x,y), radius, thickness)`

`(x, y)` is the location where the circle will be centered, and `radius` states the radial distance from our `(x, y)` location.

If we ran: `pygame.draw.circle(screen, (0, 0, 255), (50, 50), 50, 5)` we would get:

<img width="302" alt="Window5" src="https://user-images.githubusercontent.com/22228100/55438581-d88a4700-5556-11e9-91b9-bcdcf3799239.png">

