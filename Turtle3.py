import turtle 
import math
turtle.speed(1)


def reg_polygon(number_line, initial_radius):
    begin_angle = 180-(180/number_line)/2
    turtle.left(begin_angle)  

    initial_size = initial_radius*(2*math.sin(360/(2*number_line)))
    if number_line >= 3:
        sum_angle = 180*(number_line-2)
        angle = sum_angle/number_line
        for i in range(number_line):
            turtle.forward(initial_size)
            turtle.left(180-angle)
    elif number_line < 3:    
        print("Minimum number of angels should be >=3")

    
for number_line in range(3, 13):
    reg_polygon(number_line, 100) 


turtle.done()