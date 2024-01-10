#K.Hirv
#10.10.22
#Kilpkonna liikumise harjutamine
import turtle


aken = turtle.Screen()
aken.setup(300,300)
aken.bgcolor('yellow')
aken.title("Kilpkonna harjutus 03")

#konna loomine
konn1 = turtle.Turtle()
konn1.forward(100)
konn1.left(90)
konn1.forward(100)
konn1.left(90)
konn1.forward(100)
konn1.left(90)
konn1.forward(100)
konn1.penup()
konn1.left(90)
konn1.forward(100)
konn1.left(90)
konn1.forward(50)
konn1.right(90)
konn1.pendown()
konn1.forward(50)
konn1.left(90)
konn1.forward(100)
konn1.left(90)
konn1.forward(100)
konn1.left(90)
konn1.forward(100)
konn1.left(90)
konn1.forward(50)


turtle.exitonclick()
