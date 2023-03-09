l=[]
temp=[]
def leggiFile(nome_file):
    file=open(nome_file, "r")
    lista_righe= file.readlines()
    
    file.close()
    s=""
    for riga in lista_righe:
        s+=riga[:-1]
    return s

def creaListe(matrice):
    for k in range(9):
        l=[l.append(temp)*9]

def main():
    matrice=leggiFile("mappa.csv")
    print(matrice)
    creaListe(matrice)

if __name__ =="__main__": #"_" = Dunder
    main()