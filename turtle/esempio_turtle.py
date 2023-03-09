import turtle
finestra = turtle.Screen()
alice = turtle.Turtle()
bob = turtle.Turtle()

alice.color("red")
alice.forward(100)
alice.right(60)
alice.forward(100)

bob.penup()
bob.setposition(-50,50)
bob.pendown()
bob.right(90)
bob.forward(90)
turtle.done()