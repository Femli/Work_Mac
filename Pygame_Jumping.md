# Jumping in Python

One thing that is cool about programming in general is that there are many ways to solve a single problem. If you enjoy creating or brainstorming ways to tackle a given problem, and have the patience to see it through, then you will enjoy this lesson.

Jumping is a classic mechanic to teach, because there are several ways to code it. We will look at two ways to code jumping into our pygame programs:
- Linear
- Non-linear

There is a general rule that most professionals and academics like to follow, and it's known as *Occam's Razor*. Basically, follow the path that **works** and is **most simple**.

## Linear Jumping

What does linear jumping mean? In this context, it refers to how fast you jump up and how fast you fall back down. Linear here refers to the constant rate of going up and coming back down; not to be confused with the path of jumping, that is a separate mechanic.

Here is a graph to depict the linear jumping mechanic:

<img width="550" alt="Screen Shot 2019-04-11 at 2 54 05 PM" src="https://user-images.githubusercontent.com/22228100/55996021-0f551100-5c6b-11e9-84bb-833b9507b9c8.png">

As you can see by the equation `y = x`, which is a straight line, the velocity for going up is exactly the same for going down.

Here is one way of coding it:

First, we must define the variables that will govern the jumping mechanic in our program
```
jumpState = False 
lowLim = rectY 
highLim = rectY - 100
jumpCount = 20
```

Here, `jumpState = False` refers to the state of jumping. It's a boolean value, and so our player object will either be in a state of jumping or not. \
`lowLim = rectY` refers to the lowest boundry of our jump distance. Notice that it's set to the `rectY`, which is the original start position of our player object before it jumps. \
On the opposite end, `highLim = rectY - 100` refers to the highest boundry of our jump distance. Note that it is set to `rectY - 100` which means we want the total jump distance to be 100 pixels. \
`jumpCount = 20` is a variable that we need to code the jumping mechanic. We will explain it later on.

Of course, we must specify that when we press a key we want to enable the state of jumping. We will use the spacebar key in this example. Inside our events for-loop we would code the following:
```
elif event.type == pygame.KEYDOWN:
    if event.key == pygame.K_SPACE: #IF THE KEY PRESSED IS THE SPACEBAR, THEN THE RECTANGLE ENGAGE IN JUMPING
        jumpState = True
```
We start with `elif` because there is already an `if` statement before it for another mechanic. Otherwise, we would start with `if`. \

Then, outside of our events for-loop, we would code:
```
if jumpState:
    rectY -= 10
    if rectY <= highLim:
        jumpState = False
if not jumpState and rectY < lowLim :
    rectY += 10
```


