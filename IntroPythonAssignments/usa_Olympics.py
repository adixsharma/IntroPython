# Program Name: usa_Olympics.py
# Program Description: The purpose of this program is to use the turtle library to print out and draw USA OLYMPICS TEAM
# and load a image as a background as well as drawing the olympic rings and the USA flag. Name, program and date info
# are printed as well after the rings
# @author - Aditya Sharma

import turtle
import draw_Ring
import draw_USA_flag
import print_me_first


# Function name: usa_Olympics
# Function description: prints out USA then OLYMPICS TEAM below it using turtle and then places
# usa.gif (had to convert .png to type .gif) as the background image
# @param: NONE
# @return: Nothing
def drawUSA_Olympics():
    turtle.hideturtle()
    turtle.pencolor('blue')
    turtle.penup()
    turtle.left(90)
    turtle.forward(235)
    turtle.write("USA", align="center", font=("Helvetica", 60, "bold"))
    turtle.right(180)
    turtle.forward(60)
    turtle.write("OLYMPICS TEAM", align="center", font=("Helvetica", 60, "bold"))

    screen = turtle.Screen()
    # turtle.forward(60)
    screen.bgpic('usa.gif')

if __name__ == '__main__':

    drawUSA_Olympics()
    draw_USA_flag.draw_stripes()
    # draw squares to hold stars
    draw_USA_flag.draw_square()
    # draw 30 stars, 6 * 5
    draw_USA_flag.draw_six_stars_rows()
    # draw 20 stars, 5 * 4. total 50 stars representing 50 states of USA
    draw_USA_flag.draw_five_stars_rows()
    # hide the cursor/turtle
    draw_USA_flag.oogway.hideturtle()

    draw_Ring.drawRing(-270, -250, "blue")
    draw_Ring.drawRing(-180, -320, "orange")
    draw_Ring.drawRing(-90, -250, "black")
    draw_Ring.drawRing(0, -320, "dark green")
    draw_Ring.drawRing(90, -250, "red")

    msg = print_me_first.print_me_first('Aditya Sharma')
    turtle.penup()
    turtle.goto(250, -380)
    turtle.pencolor("blue")
    turtle.write(msg, font=("Helvetica", 14, ""))

    turtle.mainloop()
