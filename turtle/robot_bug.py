import turtle
import random
finestra = turtle.Screen()
robot=turtle.Turtle()
robot.speed(6)

def spostamento():
    num=random.randint(0,3)
    robot.right(num*90)
    robot.forward(10)

def main():
    for _ in range(0,10000):
        spostamento()
    turtle.done()
    
if __name__ == "__main__":
    main()

    
