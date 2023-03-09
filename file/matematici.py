def leggi_file(nome_file):
    """la funzione legge il file dei matematici"""
    file = open(nome_file,"r")
    lista_righe = file.readlines()
    file.close()

    diz_matematici = {"id":[], "nomi":[]} #id sono numeri, nomi sono str


    for riga in lista_righe[1:]:
        riga_senza_linefeed = riga[:-1]
        lista_campi=riga_senza_linefeed.split(",")
        id = int(lista_campi[0])
        nome = lista_campi[1]
        diz_matematici["id"].append(id)
        diz_matematici["nomi"].append(nome[1:])

    return diz_matematici

diz=leggi_file("./matematici.csv")
print(diz)