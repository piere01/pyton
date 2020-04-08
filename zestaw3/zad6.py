from math import sqrt
def promien(x,y,a=0,b=0):
    return sqrt((x-a)**2+(y-b)**2)
print(promien(4,9))
print(promien(2,4,2,8))