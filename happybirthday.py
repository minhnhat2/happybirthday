import turtle
import random

bg=turtle
bg.bgcolor("black")
bg.title(f"HAPPY BIRTHDAY FOR YOU")

pen=turtle.Turtle()
pen.speed(0) 
pen.color("yellow")
pen.penup()
pen.hideturtle()
pen.goto(0,200)
pen.write("HAPPY BIRTHDAY",align="center",font=("courier",20,"normal"))

turtle.penup()
turtle.goto(-170,-180)
turtle.color("magenta")
turtle.pendown()
turtle.forward(350)

turtle.penup()
turtle.goto(-160,-150)
turtle.color("white")
turtle.pendown()
turtle.forward(300)

turtle.penup()
turtle.goto(-150,-120)
turtle.color("cyan")
turtle.pendown()
turtle.forward(250)

#cake
turtle.penup()
turtle.goto(-100,-100)
turtle.color("pink")
turtle.begin_fill()
turtle.pendown()
turtle.forward(140)
turtle.left(90)
turtle.forward(95)
turtle.left(90)
turtle.forward(140)
turtle.left(90)
turtle.forward(95)
turtle.end_fill()

#candles
turtle.penup()
turtle.goto(-90,0)
turtle.color("red")
turtle.left(180)
turtle.pendown()
turtle.forward(20)

turtle.penup()
turtle.goto(-60,0)
turtle.color("blue")
turtle.pendown()
turtle.forward(20)

turtle.penup()
turtle.goto(-30,0)
turtle.color("yellow")
turtle.pendown()
turtle.forward(20)

turtle.penup()
turtle.goto(0,0)
turtle.color("green")
turtle.pendown()
turtle.forward(20)

turtle.penup()
turtle.goto(30,0)
turtle.color("purple")
turtle.pendown()
turtle.forward(20)

#decoration
colors=["red","orange","yellow","green","blue","purple","black"]
turtle.penup()
turtle.goto(-40,-50)
turtle.pendown()

for each_color in colors:
    angle=360/len(colors)
    turtle.color(each_color)
    turtle.circle(10)
    turtle.right(angle)
    turtle.forward(10)


turtle.penup()
turtle.goto(-150,50)
turtle.color("yellow")
turtle.pendown()
turtle.write("Chúc mừng sinh nhật bạn !","24pt bold")

#chanel name
def my_goto(x,y):
    turtle.pencolor("orange")
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

turtle.pendown()
my_goto(-150,150)
turtle.write('BY: @Nhatdeptrai',font=("Bradley Hand ITC",10,"bold"))
turtle.done()
