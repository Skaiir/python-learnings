import turtle

turtle.speed("fastest")

for x in range(100):
    turtle.forward(5 * x)
    turtle.left(90)

turtle.exitonclick()