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
