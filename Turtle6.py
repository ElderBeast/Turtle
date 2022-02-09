import turtle
import math
turtle.speed(1)
turtle.shape('turtle')
turtle.bgcolor("black")
turtle.pencolor("yellow")
number_line = 4
alph = 90
lenth_line = 20
pos_x = 5
pos_y = 5
for k in range(1, 10):
    for i in range(0, number_line):
        turtle.forward(lenth_line)
        turtle.left(alph)
    
    lenth_line += 10
    #turtle.right(alph)
    turtle.goto(-pos_x, -pos_y)
    pos_x += 5
    pos_y += 5
turtle.done()