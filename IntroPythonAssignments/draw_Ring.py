import turtle

def drawRing(x, y, color):
    # Named constants
    RADIUS = 70

    turtle.hideturtle()
    turtle.pensize(10)
    turtle.pencolor(color)
    turtle.penup() # when penup is set, drawing is disabled when move the cursor
    turtle.goto(x, y) # move the cursor to (x, y)
    turtle.pendown() # when pendown is setup, drawing is enabled
    turtle.circle(RADIUS) # draw a circle


