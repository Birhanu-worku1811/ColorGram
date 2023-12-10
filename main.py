import random
import turtle as turtle_module

# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract("img.png", 40)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# new_colors = []
# # Print only the list of RGB colors
# for color in rgb_colors:
#     new_colors.append(color)
#
# print(new_colors)

color_list = [(253, 251, 247), (253, 248, 252), (235, 252, 243),
              (198, 13, 32), (248, 236, 25), (40, 76, 188), (244, 247, 253),
              (39, 216, 69), (238, 227, 5), (227, 159, 49), (29, 40, 154),
              (212, 76, 15), (17, 153, 17), (241, 36, 161), (195, 16, 12),
              (223, 21, 120), (68, 10, 31), (61, 15, 8), (223, 141, 206),
              (11, 97, 62), (219, 159, 11), (54, 209, 229), (19, 21, 49),
              (238, 157, 216), (79, 74, 212), (10, 228, 238), (73, 212, 168),
              (93, 233, 198), (65, 231, 239), (217, 88, 51), (6, 68, 42),
              (176, 176, 233), (239, 168, 161), (249, 8, 48), (5, 246, 222),
              (15, 76, 110), (243, 15, 14), (38, 43, 221)]

turtle_module.colormode(255)
tin = turtle_module.Turtle()
tin.speed('fastest')
tin.penup()
tin.hideturtle()
tin.setheading(225)
tin.forward(300)
tin.setheading(0)
number_of_dots = 100

for dots_count in range(1, number_of_dots+1):
    tin.dot(20, random.choice(color_list))
    tin.forward(50)

    if dots_count % 10 == 0:
        tin.setheading(90)
        tin.forward(50)
        tin.setheading(180)
        tin.forward(500)
        tin.setheading(0)



screen = turtle_module.Screen()
screen.exitonclick()
