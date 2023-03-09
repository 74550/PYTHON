
import turtle
import math
finestra = turtle.Screen()
penna=turtle.Turtle()
penna.speed(500)
penna.pensize(10)

def poligono(posx,posy,nLati,curs,colore):
    penna.color("black")
    penna.begin_fill()
    penna.penup()
    penna.setposition(posx,posy)
    penna.pendown()
    angolo=360/nLati
    lato=2*70*math.sin(angolo/2*3.1415/180)
    for _ in range(0,nLati):
        penna.right(angolo)
        penna.forward(lato)
    penna.color(colore)
    penna.end_fill()

def main():
    diz_pos={3:(-500,100),4:(-200,100),5:(100,100),6:(400,100),7:(-450,-100),8:(-150,-100),9:(150,-100)}
    for nLati,pos in diz_pos.items():
        print(pos)
        poligono(pos[0],pos[1],nLati,penna,"violet")
    

if __name__ == "__main__":
    main()
    turtle.done()
