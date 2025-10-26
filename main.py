import turtle
import random

canvas = turtle.Screen()
canvas.screensize(300, 400, "brown")
turtle.shape("turtle")
turtle.color('brown')
turtle.pencolor('brown')
turtle.speed(1)

turtle.pendown()
list_of_colors = ['red', 'orange', 'yellow']
for i in range(1000):
    turtle.teleport(random.randint(-300, 300), random.randint(-300, 300))
    turtle.pencolor(random.choice(list_of_colors))
    for i in range(1):
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)



turtle.teleport(150, 150)
turtle.done()
turtle.penup()

turtle.mainloop()



