import turtle

t = turtle.Turtle()

t.speed(500)
colors = ["red","orange","yellow"]
turtle.Screen().bgcolor("black")

t.penup()
t.goto(-100,100)
t.pendown()
t.color("red")
t.setheading(0)
t.forward(40)
t.color("orange")
t.forward(40)
t.color("yellow")
t.forward(40)
t.color("green")
t.forward(40)


turtle.exitonclick()