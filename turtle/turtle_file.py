import turtle
import math
finestra = turtle.Screen()
penna=turtle.Turtle()
penna.speed(500)
penna.pensize(10)

def leggi_file(nome_file):
    """la funzione legge il file turtle"""
    file = open(nome_file,"r")
    lista_righe = file.readlines()
    file.close()
    
    diz_turtle = {"comandi":[], "valori":[]} 

    for riga in lista_righe:
        riga_senza_linefeed = riga
        lista_campi=riga_senza_linefeed.split(",")
        comando = lista_campi[0]
        valore = int(lista_campi[1])
        diz_turtle["comandi"].append(comando)
        diz_turtle["valori"].append(valore)
    return diz_turtle

diz=leggi_file("turtle.csv")
print(diz)

for comandi, valori in diz.items():
    for k in comandi, valori:
        if comandi[k]=="forward":
            turtle.forward(valori[k])
        if comandi[k]=="backward":
            turtle.backward(valori[k])
        if comandi[k]=="right":
            turtle.right(valori[k])
        if comandi[k]=="left":
            turtle.left(valori[k])

