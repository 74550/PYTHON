dizionario={'a':'b','b':'c','c':'d','d':'e','e':'f','f':'g','g':'h','h':'i','i':'j','j':'k','k':'l','l':'m','m':'n','n':'o','o':'p',
'p':'q', 'q':'r','r':'s','s':'t','t':'u','u':'v','v':'w','w':'x','x':'y','y':'z','z':'a',' ':' '}

dizionario2={'b':'a','c':'b','d':'c','e':'d','f':'e','g':'f','h':'g','i':'h','j':'i','k':'j','l':'k','m':'l','n':'m','o':'n','p':'o',
'q':'p', 'r':'q','s':'r','t':'s','u':'t','v':'u','w':'v','x':'w','y':'x','z':'y','a':'z',' ':' '}

parola=input("inserisci una parola: ")
parolaCodificata=""
for lettera in parola:
    parolaCodificata=parolaCodificata+dizionario[lettera]
print("parola codificata: ",parolaCodificata)

parolariCodificata=""
for lettera in parolaCodificata:
    parolariCodificata=parolariCodificata+dizionario2[lettera]
print("parola ricodificata: ",parolariCodificata)
