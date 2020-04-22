class Ksztalty:
    def __init__(self, x, y):
        self.x=x 
        self.y=y

    def pole(self):
        return self.x * self.y

    def obwod(self):
        return 2 * self.x + 2 * self.y

    def dodaj_opis(self, text):
        self.opis = text

    def skalowanie(self, czynnik):
        self.x = self.x * czynnik
        self.x = self.y * czynnik



class Kwadrat(Ksztalty):

    def __init__(self, x):
        self.x =x
        self.y=x
    
    def __str__(self):
        return 'Kwadrat o boku {}'.format(self.x)

    def __add__(self, other):
        dlugosc = self.x + other.x
        return 'Kwadrat o boku {}'.format(dlugosc)

    def __ge__(self, other):
        if (self.x >= other.x):
           return True
        return False

    def __gt__(self, other):
        if (self.x > other.x):
           return True
        return False
    
    def __le__(self, other):
        if (self.x <= other.x):
            return True
        return False

    def __lt__(self, other):
        if (self.x < other.x):
            return True
        return False


a = Kwadrat(3)
b = Kwadrat(4)
print(a + b)

if(a > b):
    print("kwadrat a jest wiekszy")
else:
    print("kwadrat b jest wiekszy")