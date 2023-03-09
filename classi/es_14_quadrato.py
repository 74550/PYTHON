class Quadrato():
    def __init__(self,x,y,lato):
        self.x=x
        self.y=y
        self.lato=lato

    def area(self):
        return self.lato * self.lato

    def perimetro(self):
        
        return self.lato * 4

    def isDentro(self,xp,yp):
        if(self.x<xp and self.x+self.lato>=xp and self.y<=yp and self.y+self.lato>=yp):
            print("interno")
        else:
            print("esterno")

def main():
    quadr=Quadrato(11,15,5)
    print(quadr.area())
    print(quadr.perimetro())
    quadr.isDentro(12,30)

if __name__=="__main__":
    main()