import turtle

turtle.speed(1)

def reset_start_point():
    # for number_line in range(3, 13):
    #     side = 100
    #     for i in range(number_line):
    #         turtle.left(360 / number_line)
    #         turtle.forward(side)
        start_pos_x = 1
        start_pos_y = 0
        
        turtle.penup()
        turtle.goto((, start_pos_y))
        turtle.pendown()   

reset_start_point()
turtle.done()   