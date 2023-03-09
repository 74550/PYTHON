from random import randint
def somma(n1,n2):
    ris=n1+n2
    return ris

def sottr(n1,n2):
    ris=n1-n2
    return ris

def molt(n1,n2):
    ris=n1*n2
    return ris

def div(n1,n2):
    ris=n1/n2
    return ris




op=int(input("inserisci nome operazione (0:addizione, 1:sottrazione, 2:moltiplicazione, 3:divisione): "))
n1=int(input("inserisci numero 1: "))
n2=int(input("inserisci numero 2: "))

diz={0:somma,1:sottr,2:molt,3:div}

print(diz[op](n1,n2))

