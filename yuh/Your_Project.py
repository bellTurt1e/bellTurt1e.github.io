"""
Write Something of your own!  This is yoru final project.
What cool designs can you make?
"""
 
import turtle, random

colors  = ["red","green","blue","orange","purple","pink","yellow"]  
turtle.delay(0)
turtle.width(10)  

length = 5

for count in range(5000):
  color = random.choice(colors)  
  turtle.forward(length)
  turtle.right(135)
  turtle.color(color)  
  length = length + 5
  
"""
When you finish, upload this file and this file only to your website!
"""
