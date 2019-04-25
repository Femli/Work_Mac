# Pygame and Time

It is no mystery that time is very important to everything we do. The very simple act of motion is relative to time, and in pygame we must learn to reference our gameplay to time.

We have all heard of the words "Frames Per Second" or *FPS* for short. If you have played video games throughout your life, then this is no strange concept. The higher frames per second we have, the smoother the gameplay should be (in theory). However, do note that high FPS isn't always the best solution. Sometimes our gameplay requires low FPS, such as when we delay movement intentionally.

We will break down how time works in pygame, and how we can use time to modify our gameplay mechanics.

## How time works in pygame

In Pygame, time is referenced as *ticks*. More specifically, ticks are measured in milliseconds. Therefore 1000 ticks is exactly 1 second. 

We can measure how many ticks have passed in our program through the following: `pygame.time.get_ticks()` \
Do note that ticks are measured after `pygame.init()` is ran. If its not ran, ticks returned will always be 0.

A way to delay time in pygame is to use the `pygame.time.delay()` method, where the argument is the amount of milliseconds we want the program to be delayed by. This in turn will cause our game mechanics to appear delayed and slowed down. 

Another way to delay our gameplay is using the `pygame.time.Clock.ticks()` method. This option is slightly more sophisticated, but the end result will be the same: slowing down the gameplay. We will break this down more specifically in the following section.

## Time delay and FPS
`pygame.time.delay()` and `pygame.time.Clock.tick()` are both methods that will delay our gameplay. However, it is important to understand how they differ. 

In `pygame.time.delay()`, we specify the amount of milliseconds (or simply, ticks) that we want to the program to be delayed by. This happens through the while loop in our program. 

Let's say we want to delay time by 60 ticks, then we would say `pygame.time.delay(60)`. We would place this line of code inside our while loop. What happens then is that all of our code will run, but the computer processor that is being used to run the game program will be assigned other tasks. Then, the computation power is split and causes our game program to be delayed by 60 ticks, as a result of sharing processor power. 

In a nutshell, the processor power that runs our program is split, and causes the program to be delayed by 60 ticks.

Now, focusing on `pygame.time.Clock.tick()` it is important to mention that this method also delays gameplay but the mechanic that it does it by is different AND makes sure that no matter how strong a computer is, the time delay will be *consistent through each machine that runs this code*.

This distinction is very important because `pygame.time.delay()` will cause time delay relative to the computation power of the machine that runs the program. That means that time will be delayed differently if you play on a 1998 Macintosh vs a 2019 Alienware...

This is where `pygame.time.Clock.tick()` comes handy, because it causes a delay in time that is *fixed* for each iteration of the while loop. In other words, if the computer is running the game too fast, and we only want it to run at 60 fps, `pygame.time.Clock.tick(60)` will make sure that the iteration of the while loop is delayed to the point where only 60 FPS are displayed in the game -- this will happen, no matter how fast the program is in other computers. However, this does not address the issue of slowness or "lag"(that's another topic).

