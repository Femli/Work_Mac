# Pygame Events and Inputs

Now that we understand more about creating and manipulating our screen display and using color and drawing tools, we can move on to more game-oriented stuff. 

In this lesson we will be breaking down how pygame handles the information that is need to create a game -- this includes everything that makes the game objects move and operate. 

We will break down the lesson as follows:
- Pygame Events
- Event Input

## Pygame Events
How do we create game objects? How can we make these objects move that way we want them to? How can we speed them up, make them disappear, change their size, or completely delete them and create new ones?

All of these questions can be further investigated by looking at how *Events* are handled in pygame. *Events* are objects in pygame that hold a list of information regarding what is going on in the program. If we move the mouse slightly, that information is captured as an *Event*; similarly, if we pressed a key in our keyboard, that is also infromation that is captured as an *Event*.

The most important type of events we will be using are:
```
QUIT             #For when we press the 'X' on the top-left or top-right button of a window 
KEYDOWN          #For when we press a key
KEYUP            #For when we let go of a key
MOUSEMOTION      #For when we move our mouse, even a little bit
MOUSEBUTTONUP    #For when we press a mouse key
MOUSEBUTTONDOWN  #For when we let go of a mouse key
```

These type of events can be further broken down into the specific keys we press on our keyboard, and the specific coordinates that our mouse pointer moves to. It all depends on how complex you want your game to be. 

### Capturing events in our pygame program
The best way to capture events in our program is by using a for-loop. Here is an example of that:
```
for event in pygame.event.get():
  print(event)
```
Let's break down what is actually happening here. 

Notice that we create a variable called `event`. The variable `event` is going to capture the list of events that are happening in our program through the method `pygame.event.get()`. Then, after an event is captured, we want to print what that exact event was. If you press any key, or if you move your mouse, you should see a bunch of information in the shell regarding those events

Let's look at another example.

Say we want to create a simple program where if we press the *W* key in our keyboard, we will print the word "pig". This is how we would do that:
```
for event in pygame.event.input():
  if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_w:
      print("pig")
```

Let's break this down once again. The `event` variable is going to be capturing all the events in our program, thanks to the method `pygame.event.input()`. Now, since we want to focus on events regarding keys being pressed, we want to make sure that the `event.type` is of the type `KEYDOWN`. If it is, then we want the specific key to be *W*, and we specify that through `event.key == pygame.K_w`. If they key being pressed down is *W*, then we want the statement "pig" to print. 

Here is a [list](https://www.pygame.org/docs/ref/key.html) of the keys we can test for.


## User Input

Now that we understand events better, let's see how we can use our input to capture events and provide game functionality. Let's say we have a small rectangle in our display. Here is the basic program for that:

```
import pygame, sys

pygame.input()
screen = pygame.display.set_mode((500, 500))

while True:
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit(); sys.exit();
    
  screen.fill((255, 255, 255))
  pygame.draw.rectangle == 
  
  TO BE CONTINUED :^))))))))))) -------------
  
