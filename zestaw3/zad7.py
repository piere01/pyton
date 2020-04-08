from math import sqrt
def przeciw(a,b=0):
    if b!=0:
        return sqrt(a**2+b**2)
    return a*sqrt(2)
print(przeciw(5))
print(przeciw(7,2))
