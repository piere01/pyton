class Ksztalty:
    def __init__(self, x, y):
        self.x=x 
        self.y=y

class Kwadrat(Ksztalty):

    def __init__(self, x):
        self.x = x
        self.y = x

    def __add__(self,other):
        aaa=self.x+other.x
        return Kwadrat(aaa)


kw1=Kwadrat(3)
print(kw1)
