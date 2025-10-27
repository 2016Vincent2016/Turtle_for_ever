import turtle as pen
import random


canvas = pen.Screen()
canvas.screensize(400, 400, "white")
pen.shape("turtle")
pen.color('black')
pen.pencolor('black')
pen.speed(100)
pen.pendown()
list_of_colors = ['cyan', 'green']

# for i in range(1000):
#     turtle.teleport(random.randint(-300, 300), random.randint(-300, 300))
#     random_stepsize = random.randint(20, 150)
#     for i in range(1):
#         turtle.circle(random_stepsize)

size = 1
for i in range (0,100):
    pen.pencolor(random.choice(list_of_colors))
    pen.circle(size)
    pen.left(5)
    size = size + 10

for i in range (0,100):
    pen.pencolor(random.choice(list_of_colors))
    pen.circle(size)
    pen.right(7)
    size = size - 10

pen.teleport(0, 0)
pen.done()
pen.penup()

pen.mainloop()





