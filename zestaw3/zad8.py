def suma(a=1,r=1,ile=10):
    if ile==1:
        return a
    return a+suma(a+r,r,ile-1)
print(suma(1,2,5))
print(suma())