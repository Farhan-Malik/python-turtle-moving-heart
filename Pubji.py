import turtle

screen = turtle.Screen()
screen.setup(500,500)
screen.tracer(0)
screen.addshape("p.gif")   # register the image with the screen as a shape

don = turtle.Turtle()
screen1=turtle.clone()
screen2=turtle.clone()
screen3=turtle.clone()
don.speed(100)
turtle.bgcolor("black")
don.shape("p.gif")
don.penup()

don.goto(-360,0)

while True :
    screen.update()
    don.forward(0.2)

   # don.right(10)