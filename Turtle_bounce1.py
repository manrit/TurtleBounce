# BY MANRIT KAUR 
# MAY 20 2022
# Turtle Bounce Assignment
from tabnanny import check
import turtle
import random

SIZE = 500
window = turtle.Screen()
window.screensize(SIZE, SIZE)
window.title("Turtle Bounce")

Turtle = turtle.Turtle()
Turtle.shape("turtle")
Turtle.penup()
Turtle.setposition(0, 0)
Turtle.forward(5)

# to get random direction from range 360
def randomDirection():
  direction = random.randrange(360)
  return direction

def Check_edges(t):
  
  while True:
    #randonDirection() method called 
    t.setheading(randomDirection())  
    
    count = 0  #number of times Turtle moved forward
    x, y = t.position()  # Get current x,y position

  
      # Keep moving until it crosses the window size of 500
     while abs(x) <= SIZE and abs(y) <= SIZE:
        t.forward(5)
        count += 1
        x, y = t.position()
  
    # Move Turtle -5 steps back
    for i in range(count):
        t.forward(-5)

Check_edges(Turtle)
window.exitonclick()