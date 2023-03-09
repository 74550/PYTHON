
def leggiFile():
    file=open("./matematici.csv")
    righe=file.readlines()
    file.close()
    diz = {"id":[], "nomi":[]}
    for riga in righe[1:]:
        campi_riga=riga[:-1].split(",")
        diz["id"].append(int(campi_riga[0]))
        diz["nomi"].append(campi_riga[1][1:])
        return diz

def nomeID(id,diz):
    listaID=diz["id"]
    listaNomi=diz["nome"]
    for i, n in zip(listaID,listaNomi):
        if(i==id):
            return n

def main():
    diz=leggiFile()
    id=2
    nome=nomeID(id,diz)
    print(nome)



if __name__=="__main__":
    main()

