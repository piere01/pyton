def parzyste(data):
    for ind in range(0,len(data)-1,2):
        yield data[ind]

Imie=parzyste("michał")
print(next(Imie))
print(next(Imie))
print(next(Imie))

