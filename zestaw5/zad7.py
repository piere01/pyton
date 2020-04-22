class Parzyste:
    def __init__(self, data):
        self.data = data
        self.ind = -2

    def __iter__(self):
        return self

    def __next__(self):
        self.ind +=2
        if self.ind >= len(self.data):
            raise StopIteration
        return self.data[self.ind]

Imie=Parzyste("Kalamalaka")
par=iter(Imie)
print(next(par))
print(next(par))
print(next(par))
print(next(par))
print(next(par))
