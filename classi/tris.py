import turtle
tabella=turtle.Turtle()
x=turtle.Turtle()
o=turtle.Turtle()
finestra = turtle.Screen()
tabella.pensize(10)
x.pensize(10)
o.pensize(10)

class Tris():
    def creaTabella(self):
        tabella.penup()
        tabella.setposition(100,100)
        tabella.pendown()
        tabella.right(90)
        tabella.forward(300)

        tabella.penup()
        tabella.setposition(0,100)
        tabella.pendown()
        tabella.forward(300)

        tabella.penup()
        tabella.setposition(200,20)
        tabella.pendown()
        tabella.right(90)
        tabella.forward(300)

        tabella.penup()
        tabella.setposition(200,-100)
        tabella.pendown()
        tabella.forward(300)

    def inserisciSegno(self):
        cont = 0
        sommapos1 = 0
        sommapos2 = 0
        win = False
        while(win == False and cont < 9):
            if(cont%2==0):
                posiz1=int(input("giocatore 1 inserisci posizione: "))
                Tris.disegnaSegno(self,posiz1,"x")
                cont=cont+1
                sommapos1=sommapos1+posiz1
                
            else:
                posiz2=int(input("giocatore 2 inserisci posizione: "))
                Tris.disegnaSegno(self,posiz2,"o")
                cont=cont+1
                sommapos2=sommapos2+posiz2
            
            if(sommapos1%6==0):
                win = True
                print("fine")
            if(sommapos2!=0):
                if(sommapos2%6==0):
                    win = True
                    print("fine")

    def disegnaSegno(self, posiz,simbolo):
        if(simbolo=="o"):
            if(posiz==1):
                o.penup()
                o.setposition(-50,50)
                o.pendown()
                o.circle(30)
            if(posiz==2):
                o.penup()
                o.setposition(50,50)
                o.pendown()
                o.circle(30)
            if(posiz==3):
                o.penup()
                o.setposition(150,50)
                o.pendown()
                o.circle(30)
            if(posiz==4):
                o.penup()
                o.setposition(-50,-50)
                o.pendown()
                o.circle(30)
            if(posiz==5):
                o.penup()
                o.setposition(50,-50)
                o.pendown()
                o.circle(30)
            if(posiz==6):
                o.penup()
                o.setposition(150,-50)
                o.pendown()
                o.circle(30)
            if(posiz==7):
                o.penup()
                o.setposition(-50,-170)
                o.pendown()
                o.circle(30)
            if(posiz==8):
                o.penup()
                o.setposition(50,-170)
                o.pendown()
                o.circle(30)
            if(posiz==9):
                o.penup()
                o.setposition(150,-170)
                o.pendown()
                o.circle(30)
        elif(simbolo=="x"):
            if(posiz==1):
                x.penup()
                x.setposition(-90,100)
                x.pendown()
                x.right(45)
                x.forward(100)
                x.penup()
                x.setposition(-90,40)
                x.pendown()
                x.left(90)
                x.forward(100)
                x.right(45)
            if(posiz==2):
                x.penup()
                x.setposition(10,100)
                x.pendown()
                x.right(45)
                x.forward(100)
                x.penup()
                x.setposition(10,40)
                x.pendown()
                x.left(90)
                x.forward(100)
                x.right(45)
            if(posiz==3):
                x.penup()
                x.setposition(110,100)
                x.pendown()
                x.right(45)
                x.forward(100)
                x.penup()
                x.setposition(110,40)
                x.pendown()
                x.left(90)
                x.forward(100)
                x.right(45)
            if(posiz==4):
                x.penup()
                x.setposition(-90,0)
                x.pendown()
                x.right(45)
                x.forward(100)
                x.penup()
                x.setposition(-90,-60)
                x.pendown()
                x.left(90)
                x.forward(100)
                x.right(45)
            if(posiz==5):
                x.penup()
                x.setposition(10,0)
                x.pendown()
                x.right(45)
                x.forward(100)
                x.penup()
                x.setposition(10,-60)
                x.pendown()
                x.left(90)
                x.forward(100)
                x.right(45)
            if(posiz==6):
                x.penup()
                x.setposition(110,0)
                x.pendown()
                x.right(45)
                x.forward(100)
                x.penup()
                x.setposition(110,-60)
                x.pendown()
                x.left(90)
                x.forward(100)
                x.right(45)
            if(posiz==7):
                x.penup()
                x.setposition(-90,-120)
                x.pendown()
                x.right(45)
                x.forward(100)
                x.penup()
                x.setposition(-90,-180)
                x.pendown()
                x.left(90)
                x.forward(100)
                x.right(45)
            if(posiz==8):
                x.penup()
                x.setposition(10,-120)
                x.pendown()
                x.right(45)
                x.forward(100)
                x.penup()
                x.setposition(10,-180)
                x.pendown()
                x.left(90)
                x.forward(100)
                x.right(45)
            if(posiz==9):
                x.penup()
                x.setposition(110,-120)
                x.pendown()
                x.right(45)
                x.forward(100)
                x.penup()
                x.setposition(110,-180)
                x.pendown()
                x.left(90)
                x.forward(100)
                x.right(45)

def main():
    tris = Tris()
    tris.creaTabella()
    print("giocatore 1: giochi con x")
    print("giocatore 2: giochi con o")
    tris.inserisciSegno()


if __name__ == "__main__":
    main()
    turtle.done()

