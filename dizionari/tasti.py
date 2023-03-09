dizionario={"w":"avanti","a":"sinistra","s":"indietro","d":"destra", "i":"avanti", "j":"sinistra", "k":"indietro", "l":"destra"}

comando="avanti"

l=[]

for indice, azione in dizionario.items():
    if azione==comando :
        l.append(indice)
print(l)
    

