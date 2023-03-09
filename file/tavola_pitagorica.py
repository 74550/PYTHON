def make_tabella():
    return[[numero*indice for numero in range(1,11)for indice in range(1,11)]]

def write_file(nomeFile, tabella):
    file=open(nomeFile,"w")
    for riga in tabella:
        file.write(f'{riga}\n')
    file.close()

def main():
    tabella=make_tabella()
    write_file("tabella_pitagorica.txt",tabella)

if __name__ == "__main__":
    main()
