import turtle
finestra = turtle.Screen()
penna=turtle.Turtle()
penna.speed(100)

def leggi_file(nome_file):
    file = open(nome_file,"r")
    lista_righe = file.readlines()
    file.close()
    s=""
    for riga in lista_righe:
        s+=riga[:-1]
    print(s)
    return s

def disegna(file):
        for carattere in file:
            if(carattere=='A'):   
                penna.forward(10)
            elif(carattere=='T'):
                penna.backward(10)
            elif(carattere=='C'):
                penna.left(90)
                penna.forward(100)
            elif(carattere=='G'):
                penna.right(90)
                penna.forward(10)
            
def main():
    leggi_file("./covid-19_gen1.txt")
    disegna(leggi_file("./covid-19_gen1.txt"))

if(__name__=="__main__"):
    main()
    turtle.done()


