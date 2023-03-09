lista=[110,12,45,23,66]

#modo preferito (pythonico)
for elemento in lista:
    print(elemento,end="-")
print("")
#modo c-style
for i in range (0,len(lista)):
    print(lista[i],end="-")
print("")

#calcolo massimo e minimo in modo pythonico

minimo=lista[0]
massimo=lista[0]

for elemento in lista[1:]:
    if (elemento>massimo):
        massimo=elemento
    else:
        pass
    if(elemento<minimo):
        minimo=elemento
print(minimo,massimo)