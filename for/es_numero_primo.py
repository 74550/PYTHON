def isPrimo(x):
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
    return True

n = int(input("inserisci un numero maggiore di 0: "))
if isPrimo(n)==True:
    print("numero primo")
else: 
    print("non primo")




