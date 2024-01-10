#K.Hirv
#10.10.22
#Kilpkonna liikumise harjutamine
import turtle


aken = turtle.Screen()
aken.setup(300,300)
aken.bgcolor('yellow')
aken.title("Kilpkonna harjutus 01")

#konna loomine
konn1 = turtle.Turtle()
konn1.color("lime")
konn1.forward(100)
konn1.penup()
konn1.left(180)
konn1.pendown()
konn1.forward(100)
konn1.left(45)
konn1.forward(100)

konn2 = turtle.Turtle()
konn2.color("red")
konn2.right(90)
konn2.forward(100)
konn2.penup()
konn2.left(180)
konn2.pendown()
konn2.forward(100)
konn2.right(45)
konn2.forward(100)

konn3 = turtle.Turtle()
konn3.color("orange")
konn3.left(90)
konn3.forward(100)
konn3.penup()
konn3.left(180)
konn3.pendown()
konn3.forward(100)
konn3.left(45)
konn3.forward(100)

konn4 = turtle.Turtle()
konn4.color("blue")
konn4.penup()
konn4.left(180)
konn4.pendown()
konn4.forward(100)
konn4.penup()
konn4.left(180)
konn4.forward(100)
konn4.left(135)
konn4.pendown()
konn4.forward(100)

turtle.exitonclick()
