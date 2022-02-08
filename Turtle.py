import turtle


turtle.shape('turtle')
angle = 20
n = 1
for i in range(100):
    turtle.forward(i)
    turtle.left(angle)
    n += 1