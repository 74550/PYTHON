import turtle  #importo libreria
barra=turtle.Turtle()  #creo la turtle
finestra = turtle.Screen()  #creo la finestra
barra.pensize(4) #larghezza barra

class Barcode():
    def traduciStringa(self, str):
        stringa_unicode=[]
        stringa_bin=[]
        s=""
        for carattere in str:
            stringa_unicode.append(ord(carattere))    #aggiungo alla lista i caratteri unicode convertiti dalla stringa
        print(stringa_unicode)
        for numero in stringa_unicode:
            numero=bin(numero)
            stringa_bin.append(numero[2:])       #aggiungo alla lista i caratteri binari convertiti dalla lista unicode
        print(stringa_bin)

        for i in stringa_bin:
            s += "0" * (8 - len(i)) + i      #scrivo il contenuto della lista come stringa
        print(s) 
        return s

    def disegna(self,str_bin):
        barra.right(90)
        k=0
        for numero in str_bin:
            if(int(numero)==1):   #se c'è 1 disegno una riga nera
                barra.setposition(k,0)
                barra.pendown()
                barra.color("black")
                barra.forward(100)
                barra.penup()
                k=k+7
            else:
                barra.setposition(k,0)    #se c'è 1 disegno una riga bianca
                barra.pendown()
                barra.color("white")
                barra.forward(100)
                barra.penup()
                k=k+7

        
            




def main():
    codice_a_barre = Barcode()
    stringa=input("inserisci stringa: ")
    stringa_binaria=codice_a_barre.traduciStringa(stringa)
    codice_a_barre.disegna(stringa_binaria)

if __name__ == "__main__":
    main()
    turtle.done()
