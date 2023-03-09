from turtle import *
from time import sleep

dim = int(input("dimensione: "))

Screen().title("indovina cos'è")
Screen().bgcolor("red")
penup()
goto(-dim / 6, dim / 2 - dim / 3)
pendown()

begin_fill()
for k in range(4):
    left(90)
    forward(dim / 3 * 2)
    right(90)
    forward(dim)
    right(90)
    forward(dim / 3)
    right(90)
    forward(dim / 3 * 2)
    left(90)
    forward(dim / 3)
end_fill()

colors = ("blue", "orange", "yellow", "white", "lightblue", "grey", "green", "red")

while True:
    for c in colors:
        Screen().bgcolor(c)
        sleep(0.15)