def fiboc(maksymalna):
    x=0
    y=1
    while y<maksymalna:
        yield y
        temp=x+y
        x=y
        y=temp

aa=fiboc(100000)
print(next(aa))
print(next(aa))
print(next(aa))
print(next(aa))
print(next(aa))
print(next(aa))
print(next(aa))
print(next(aa))
print(next(aa))
print(next(aa))
print(next(aa))
print(next(aa))
print(next(aa))
print(next(aa))
print(next(aa))
print(next(aa))
print(next(aa))
print(next(aa))
print(next(aa))
print(next(aa))
print(next(aa))
