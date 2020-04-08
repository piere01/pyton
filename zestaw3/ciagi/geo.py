def wyraz(a=1,r=1,ktory=1):
    if ktory==1:
        return a
    return wyraz(a*r,r,ktory-1)

def suma(a=1,r=1,ile=10):
    if ile==1:
        return a
    return a+suma(a*r,r,ile-1)

def iloczyn(a=1,r=1,ile=10):
    if ile==1:
        return a
    return a*iloczyn(a*r,r,ile-1)