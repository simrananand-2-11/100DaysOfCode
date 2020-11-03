# Write a program to print patter of Star, rectangle, octagon, pentagon, using turtle.
'''
import turtle
 
# Starting a Working Screen
ws = turtle.Screen()
 
# initializing a turtle instance
geekyTurtle = turtle.Turtle()
 
# executing loop 5 times for a star
for i in range(5):
 
        # moving turtle 100 units forward
        geekyTurtle.forward(100)
 
        # rotating turtle 144 degree right
        geekyTurtle.right(144)
'''
'''
import turtle 
  
# creating turtle pen 
t = turtle.Turtle() 
  
# taking input for the no of the sides of the polygon 
n = int(input("Enter the no of the sides of the polygon : ")) 
  
# taking input for the length of the sides of the polygon 
l = int(input("Enter the length of the sides of the polygon : ")) 
  
  
for _ in range(n): 
    turtle.forward(l) 
    turtle.right(360 / n) 
'''
# Create Chat application using client and server programming.
