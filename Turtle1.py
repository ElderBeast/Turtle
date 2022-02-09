import turtle
import math


def prav_mnog():
    """paint right triangle"""
    turtle.shape('turtle')
    turtle.bgcolor("black")
    turtle.pencolor("yellow")
    for number_line in range(3, 13):
        alph = 360 / number_line
        for i in range(0, number_line):
            turtle.forward(line)
            turtle.left(alph)
            print(i)
        turtle.penup()        
        turtle.forward(line)
        turtle.pendown()


def ten_triangle():
    number_frame = 0
    while number_frame <= 10:
        prav_mnog()
        number_frame += 1
    print(number_frame)


ten_triangle()