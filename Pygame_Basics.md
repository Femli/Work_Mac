# Introduction to Pygame

Now that we have completed all the pre-requisites for pygame, you should all be EXPERTS at python :^) \
We can now move on to pygame stuff.

At first, all this information may seem overwhelming, but rest assured that indeed it really is overwhelming :D

No but seriously, it might get tough but don't give up! We are almost done

## Major python components

There are several components that make up a basic pygame program. For now, we will go over only the most important stuff. It is important for you to practice these because they will almost always be present in every pygame program!



`import` - Is a statement that tells python to import a module. A module is a .py file inside the python library. \
`import pygame` - The pygame module contains many classes and data structures for creating a game! If we didn't use this, we would be writing thousands and thousands lines of code... no thanks. \
`import sys` - The sys module allows us to fully terminate a python program. 


`pygame.init()` - The most important pygame method: it allows us to start the pygame program. \
`pygame.display.set_mode(())` - This is where we set the size of our game screen window. \
`pygame.display.update()` - Everytime we run this method, the screen display will update our changes -- Also known as _double buffering_, which enables us to update the game every single frame. \
`while True:` - The majority of our game code will be inside an infinite while loop. This is important for many reasons, which will be highlighted later. 

Now that we have covered some of the most common methods used, here is an example of a very simple pygame program you can run.

```
# ALL THIS CODE WILL BE INSIDE THE WHILE LOOP

for event in pygame.event.get():
        if event.type == pygame.QUIT:
             pygame.quit(); sys.exit();
```
The purpose of this program is very simple: to terminate the pygame program when we press the "X" red button on the top-left or top-right of the window. 

Let's further break down this program: \
`pygame.event.get()` - Collects all the events that the program records. Since `pygame.event.get()` is ran
each iteration of the for-loop, the variable `event` will collect the events happening in the pygame program. By events we mean everything we do on the screen and keyboard. It captures the location of our mouse cursor, and the keys that we press. \
The if-else statement is there to let us know when the event of pressing the close window happens. Then, `pygame.quit()` and will close down the python application and `sys.exit()` will shut down the infinite loop, effectively killing the entire application and game in the process.


