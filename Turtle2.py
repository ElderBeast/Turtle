import turtle
import math
turtle.speed(1)
turtle.shape('turtle')
turtle.bgcolor("black")
turtle.pencolor("yellow")


def prav_mnog():
    """paint right triangle"""
    side = 40
    pos_x = 10
    pos_y = 20
    
    for number_line in range(3, 13):
        for i in range(0, number_line):
            turtle.left(360/number_line)
            turtle.forward(side)
        side += 20
        turtle.penup()
        turtle.goto(pos_x, -pos_y)
        pos_x += 10
        pos_y += 20
        turtle.pendown()
            

prav_mnog()

turtle.done()