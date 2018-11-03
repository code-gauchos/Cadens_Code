import turtle


turtle.bgcolor("black")
Turtlepen = turtle.Pen()

Turtlepen.pencolor("yellow")

for counter in range (10000):
   Turtlepen.forward(counter)
   Turtlepen.left(20)
   if(counter == 50):
        turtle.bgcolor("blue")
   else:
        turtle.bgcolor("purple")