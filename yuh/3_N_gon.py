
"""
Create a function that will draw a regular polygon with 'n' sides.
This function should have 2 parameters:
  (s) for side length
  (n) for number of sides
* Make sure to compute the angle after the number of sides is given using 360/n
"""
import turtle
sven = turtle.Turtle()
  
def polygon (n):
    for i in range(6):
       sven.forward(100)
       sven.right(60)
polygon(10)

