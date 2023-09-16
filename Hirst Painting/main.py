import turtle as t
import random

x = t.Turtle()
t.colormode(255)
x.speed("fastest")
x.penup()
x.hideturtle()
color_list = [(197, 165, 117), (142, 80, 56), (220, 201, 137), (59, 94, 119), (164, 152, 53),
              (136, 162, 181), (131, 34, 22), (69, 39, 32), (53, 117, 86), (192, 95, 78),
              (146, 177, 149), (19, 91, 68), (165, 143, 157), (31, 59, 76), (111, 75, 81),
              (228, 176, 164), (128, 29, 33), (179, 204, 177), (71, 34, 36), (25, 82, 89),
              (89, 146, 127), (18, 69, 57), (41, 66, 90), (219, 178, 182), (175, 94, 98), (179, 192, 205)]

x.setheading(225)
x.forward(300)
x.setheading(0)
num_of_dots = 100
       
for dot_count in range(1, num_of_dots + 1):
    x.dot(20, random.choice(color_list))
    x.forward(50)
    if dot_count % 10 == 0:
        x.setheading(90)
        x.forward(50)
        x.setheading(180)
        x.forward(500)
        x.setheading(0)

s = t.Screen()
s.exitonclick()
