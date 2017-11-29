"""
1. Create a function that will draw a Square - call it DrawSquare()
2. Allow this function to have 1 Parameter (s) for the side length.
3. Use a FOR Loop for this function.
"""
import turtle
sven = turtle.Turtle()
turtle.delay(20)
 
def DrawSquare(s):
    
    for i in range(4):
        sven.forward(100)
        sven.right(90)

DrawSquare(10)
 




"""
4. Inside a for loop, call the Square function 100 times,
for the sidelength of 10*i.

5.  Using the pen up and pendown functions (YourTurtle.pu()) use the .goto(x,y)
to move the turtle before drawing the next square.  Try and see if you can get it
to make all the squares share the same center.
"""
#4
sven.pu()
sven.goto(1,2)
sven.pd()
def square():
    for i in range(100):
        
        sven.forward(100)
        sven.right(90)
        
square()

"""
    for i in range():


return i


#5
    """
