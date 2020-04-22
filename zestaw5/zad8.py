class Samo:
    __samo={"a","e","y","i","o","u"}

    def __init__(self, data):
        if isinstance(data,str):
            self.data = data
        else:
            self.data=str(data)
        self.ind = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.ind +=1
        if self.ind >= len(self.data):
            raise StopIteration
        if self.data[self.ind] in Samo.__samo:
            return self.data[self.ind]

Klaw=Samo("garedypoluki")
rak=iter(Klaw)
print(next(rak))
print(next(rak))
print(next(rak))
print(next(rak))
print(next(rak))
print(next(rak))
print(next(rak))
print(next(rak))
print(next(rak))
print(next(rak))
print(next(rak))
print(next(rak))
kar=Samo(153)
let=iter(kar)
print(next(kar))
print(next(kar))
print(next(kar))
