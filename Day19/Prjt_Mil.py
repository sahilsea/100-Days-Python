# import colorgram

# colors = colorgram.extract('images-2.jpeg', 20)

# rgb_colors = []
# for color in colors:
#     red = color.rgb.r
#     green = color.rgb.g
#     blue = color.rgb.b
#     rgb_colors.append((red, green, blue))

# print(rgb_colors)
import turtle
import random


tim = turtle.Turtle()
tim.speed('fastest')
turtle.colormode(255)
tim.pensize(10)
tim.penup()



color_list = [ (120, 178, 209), (225, 157, 88), (211, 130, 166), (191, 172, 20), (233, 206, 98), (37, 113, 163), (169, 15, 48), (215, 76, 115), (31, 141, 77), (17, 170, 206), (201, 67, 28), (23, 181, 146), (168, 54, 95), (234, 76, 48), (241, 162, 190), (14, 29, 77)]


n = 40

for i in range(1, 9):
    for i in range(0, 10):
        tim.dot(20, random.choice(color_list))
        tim.forward(40)
    n += 40
    tim.sety(n)
    tim.setx(0)

















screen = turtle.Screen()
screen.exitonclick()