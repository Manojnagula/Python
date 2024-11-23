import turtle
import random

my_turtle = turtle.Turtle()
turtle.colormode(255)
my_turtle.shape('turtle')
my_turtle.color('green')
my_turtle.pensize(8)
my_turtle.speed(10)

def random_colour():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    return (r,g,b)

# my_turtle.forward(100)
# my_turtle.right(90)
# my_turtle.forward(100)
# my_turtle.right(90)
# my_turtle.forward(100)
# my_turtle.right(90)
# my_turtle.forward(100)

# dashed line
# for i in range(10):
#     my_turtle.forward(10)
#     my_turtle.penup()
#     my_turtle.forward(10)
#     my_turtle.pendown()

# shapes
# for i in range(3,11):
#     my_turtle.color(random.choice(colors))
#     for j in range(i):
#         my_turtle.forward(100)
#         my_turtle.right(360/i)

# random walk
# angle = [90,180,270,360]
# for i in range(100):
#     my_turtle.color(random_colour())
#     my_turtle.forward(35)
#     my_turtle.right(random.choice(angle))
    
# spirograph
# my_turtle.pensize(1)
# my_turtle.speed('fastest')
# for i in range(360//5):
#     my_turtle.color(random_colour())
#     my_turtle.circle(100)
#     my_turtle.right(5)

# hirst spot painting


screen = turtle.Screen()
screen.exitonclick()