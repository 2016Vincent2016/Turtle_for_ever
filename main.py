import turtle
import random

canvas = turtle.Screen()
canvas.screensize(400, 400, "#C20C1E")
turtle.shape("turtle")
turtle.color('brown')
turtle.pencolor('brown')
turtle.speed(10000000000000000000000000000000000000000000000000000000000000000000000)

turtle.pendown()
list_of_colors = ['red', 'orange', 'yellow']
for i in range(1000):
    turtle.teleport(random.randint(-300, 300), random.randint(-300, 300))
    turtle.pencolor(random.choice(list_of_colors))
    random_stepsize = random.randint(1, 350)
    for i in range(4):
        turtle.forward(random_stepsize)
        turtle.left(90)




turtle.teleport(150, 150)
turtle.done()
turtle.penup()

turtle.mainloop()





