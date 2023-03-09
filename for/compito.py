lista1=["a","b","c","d"]
lista2=[1,2,3,4]

#for su lista1 C-style
for indice in range(0,len(lista1)):
    print(lista1[indice],end="-")
print("")

#for su lista1 Python-style
for elemento in lista1:
    print(elemento,end="-")
print("")
#for su lista1 con enumerate
for indice, elemento in enumerate(lista1):
    print(elemento,end="")
print("")
#for su lista1 e 2 Python-style(zip)
l1=[]
l2=[]
for elementi1, elementi2 in zip(lista1,lista2):
    l1.append(elementi1)
    l2.append(elementi2)
print(l1)
print(l2)
#for su lista1 e 2 C-style(range...)
l3=[]
l4=[]
for indice in range(0,len(lista1)):
    l3.append(lista1[indice])
    l4.append(lista2[indice])
print(l3)
print(l4)

diz={1:"Abello",2:"Armando"}

#for su diz usando items()
for chiave, valore in diz.items():
    print(chiave, valore)
#for su diz senza items()
for chiave in diz:
    print(chiave, diz[chiave])