import colorgram
import turtle
import random
# colors = colorgram.extract(r'c:\Users\Manoj\Downloads\damien_hirst.webp',30)
# rgb_colors = []
# for color in colors:
#     rgb_colors.append((color.rgb.r,color.rgb.g,color.rgb.b))
# print(rgb_colors)

color_list=[
    (230, 240, 247), (236, 223, 83), (205, 5, 69), (202, 74, 12), (111, 181, 218), (197, 164, 10), (217, 161, 109), (235, 50, 131), (235, 224, 6), (15, 29, 175), (29, 189, 114), (13, 23, 63), (23, 106, 174), (213, 136, 177), (9, 185, 215), (207, 27, 143), (228, 168, 201), (122, 191, 163), (66, 22, 7), (8, 49, 28), (189, 15, 5), (31, 136, 73), (127, 218, 232), (56, 10, 33), (144, 216, 201), (111, 89, 211), (235, 63, 38)]
turtle.colormode(255)
my_turtle = turtle.Turtle()
my_turtle.pensize(10)
my_turtle.penup()
my_turtle.setheading(225)
my_turtle.forward(250)
my_turtle.setheading(0)
my_turtle.hideturtle()
my_turtle.speed('fastest')

for i in range(1,100+1):
    my_turtle.dot(20,random.choice(color_list))
    my_turtle.forward(50)
    if i%10==0:
        my_turtle.setheading(90)
        my_turtle.forward(50)
        my_turtle.setheading(180)
        my_turtle.forward(500)
        my_turtle.setheading(0)


screen =turtle.Screen()
screen.exitonclick()