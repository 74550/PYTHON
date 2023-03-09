class Robot():
    def __init__(self,nome,massa,tipo):
        self.nome=nome #stringa
        self.massa= massa  #float
        self.tipo=tipo   #stringa

    def stampaNome(self):
        print(self.nome)

    def pericolo(self):
        if(self.massa>100 and self.tipo=="umanoide"):
            return True
        else: 
            return False

def main():
    robot=Robot("Leonardo",150,"umanoide")
    robot.stampaNome()
    if(robot.pericolo()==True):
        print("robot pericoloso")
    else:
        print("robot innocuo")

if __name__=="__main__":
    main()