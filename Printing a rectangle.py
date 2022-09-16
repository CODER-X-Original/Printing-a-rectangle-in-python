from shutil import move
import turtle 

move = turtle.Turtle()

move.color("red") # Choose colour from here
move.pensize(5) # Size of your pen
move.shape('turtle')

def making_a_square() :
 move.forward(300)
 move.right(90)
 move.forward(150)
 move.right(90)
 move.forward(300)
 move.right(90)
 move.forward(150)
 move.right(90)
 

making_a_square()