n=int(input("inserisci numero: "))
l=[]
for i in range(1,n+1):      #posso usare la list comprehension per fare la stessa cosa
    l.append(i)
print(l)

list=[i for i in range(1,n+1)]     #list comprehension
print(list)
