"""
1. Create a loop that does something turn and some distance forward 255 times.
2. Create a window (using the turtle.Screen() function) and change the colormode to 255
3. Create three variables, r, g, b and set them all = 0.
4. Inside your loop, allow ONE of these parameters to add 1 each time.
5. If you want to change more than one color, how could you do that?
6. Try and change the colors from black to red to green to blue all inside one completion of the Loop
 ** Hint: Use IF statements to evaluate the value of i (the loop variable) before adding or subtracting from r,g,b
 """
import turtle
from random import randint
joe = turtle.Turtle()
sven = turtle.Turtle()
sven.speed(0)
joe.speed(0)
wn = turtle.Screen()
wn.colormode(255)
turtle.delay(0)

turtle.bgcolor("Black")

 
 
r = 220
g = 150
b = 50

for i in range(2000):
     
    joe.forward(5+i)
    joe.left(88)
    joe.color(r, g, b)
    sven.forward(5+i)
    sven.left(98)
    sven.circle(50)
    joe.circle(50)
    sven.color(r, g, b)
    while r>0:
        r = r - 1
    if r == 0 and b < 255:
        b = b+1
    if b == 255 and g > 0:
        g = g - 1
    if  g == 0:
        r = r + 1
        
 
