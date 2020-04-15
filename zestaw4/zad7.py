class Robak():
    x=0
    y=0
    krok=1


    def __init__(self, x, y, z):
        self.x=x
        self.y=y
        self.krok=z

    def w_gore(self, ile):
        self.y+=ile*self.krok
    
    def w_dol(self, ile):
        self.y-=ile*self.krok

    def w_prawo(self, ile):
        self.x+=ile*self.krok
    
    def w_lewo(self, ile):
        self.x-=ile*self.krok

    def gdzie_jestes(self):
        print("X: ",self.x,", Y: ",self.y)



karol=Robak(1,5,7)
karol.gdzie_jestes()
karol.w_gore(6)
karol.gdzie_jestes()
karol.w_dol(12)
karol.gdzie_jestes()
karol.w_prawo(7)
karol.gdzie_jestes()
karol.w_lewo(12)
karol.gdzie_jestes()