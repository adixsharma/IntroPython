import turtle
import time
import os
import sys
from datetime import datetime
"""
Sample program on drawing various shapes using turtle and write
text on the screen

This may be useful to help you doing your lab assignment
"""


trtl=turtle.Turtle()
trtl.pencolor('red')     #making colour of the pen red
trtl.pensize(5)     #choosing the size of pen nib 
#trtl.speed(1)     #choosing the speed of drawing
trtl.shape('turtle')    #choosing the shape of pen n
n=3    #starting for drawing a triangle
OFFSET=3
shapes=['Triangle','Square','Pentagon','Hexagon','Heptagon','Octagon','Nonagon','Decagon']

while n<11: #    limiting to a decagon 11
#    print("n=", n)
    trtl.clear()

    trtl.penup()
    trtl.goto(0,100)
    trtl.pendown()
    trtl.write(shapes[n-OFFSET], align = "center", font = ("Helvetica", 60, "bold"))
    trtl.penup()
    trtl.goto(0,0)
    trtl.pendown()

    
    for i in range(n):     # for loop to minimize the same lines of codes being written
        trtl.pencolor('blue')
        trtl.forward(60)     #top line
        trtl.right(360/n) 
    n=n+1
    trtl.penup()
    trtl.home()
    trtl.pendown()
    trtl.penup() 
    trtl.home()    #moving the turtle to make the animation more centric 
    trtl.pendown()
    trtl.ht()
#    time.sleep(1)
    trtl.st()

trtl.penup()
trtl.goto(300,-300)
trtl.pendown()
trtl.pencolor('green')
trtl.ht()
program = os.path.basename(sys.argv[0])
msg = "Program: " + program + "\nHave a nice day!\n"
trtl.write(msg, align = "right", font = ("aerial", 12, "italic"))
