import turtle


turtle.bgcolor("black")
Turtlepen = turtle.Pen()


# "light green","brown"
Colors=["red","blue","yellow","orange","purple","white"]

for counter in range (10000):
   Turtlepen.pencolor(Colors[counter%6])
   Turtlepen.forward(counter)
   Turtlepen.left(210)
