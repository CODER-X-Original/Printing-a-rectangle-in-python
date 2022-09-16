from shutil import move
import turtle 

move = turtle.Turtle()

move.color("red") # Choose colour from here
move.pensize(5) # Size of your pen
move.shape('turtle')

def making_a_rectangle() :
 move.forward(300) # The size of the line
 move.right(90) # Angle 
 move.forward(150) # The size of the line
 move.right(90) # Angle
 move.forward(300) # The size of the line
 move.right(90) # Angle
 move.forward(150) # The size of the line
 move.right(90) # Angle
 

making_a_rectangle()