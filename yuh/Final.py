"""
Import your n_gon file using:
  from n_gon import *

We are going to call the function inside a FOR loop using i as the number of sides (n)
*Don't forget to import turtle and create a Turtle() to be used in this
1.  Add from random import randint
2.  Create a color list: colors = ["Blue", "Green", "Red", "Black", "Yellow", "Purple"]
3.  Can you figure out how to change the colors randomly using this list?
4.  Write a for loop that would change the colors and the size of the squares randomly
5.  Add a turn of some random angle after each statement you call the n-gon.
6.  Make a for loop with 100 random shapea of colors and number of sides?
"""
import turtle
import random
turtle.delay(0)
sven = turtle.Turtle()
sven.speed(0)
colors = ["Blue", "Green", "Red", "Black", "Yellow", "Purple"] 
sven.pensize(10)
turtle.bgcolor
("Black")
 
 
def Square(s):               
    for i in range(4):
        num = random.randint(0,5)
        sven.color(colors[num])
        sven.forward(s)
        sven.right(72)
        for i in range(4):
                num = random.randint(1,5)
                sven.color(colors[num])
                sven.forward(s)
                sven.right(180)
                for i in range(4):
                        num = random.randint(0,5)
                        sven.color(colors[num])
                        sven.forward(s)
                        sven.right(80)
    
    
for n in range(100):
    sven.pu() 
    sven.goto(-5 * n, 5 * n )
    sven.pd()
    Square(10 * n)

 
 
