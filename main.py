import turtle

screen = turtle.Screen()
screen.setup(500,500)
screen.tracer(0)
screen.addshape("heart 02.gif")   # register the image with the screen as a shape

don = turtle.Turtle()
screen1=turtle.clone()
screen2=turtle.clone()
screen3=turtle.clone()
don.speed(200)
turtle.bgcolor("black")
don.shape("heart 02.gif")
screen1.shape("heart 02.gif")# now set the turtle's shape to it
screen2.shape("heart 02.gif")
screen3.shape("heart 02.gif")
don.penup()

don.goto(0,180)
screen1.penup()
screen1.goto(0,0)
screen2.penup()
screen2.goto(270,-180)

screen3.penup()
screen3.goto(360,-0)

while True :
    screen.update()
    don.right(1.11)

    don.forward(1.11)
    screen1.left(1.11)
    screen1.backward(1.11)
    screen2.left(1.11)
    screen2.backward(1.11)
    screen3.right(1.11)
    screen3.forward(1.11)
    don.right(10)