def print_hello():
    print("hello world")

print_hello()

import turtle

screen = turtle.Screen()
screen.bgcolor("black")

star = turtle.Turtle()
star.color("yellow")
star.speed(5)

for i in range(5):
    star.forward(200)
    star.right(144)

screen.exitonclick()
