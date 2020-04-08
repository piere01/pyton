def iloczyn(a=1,r=1,ile=10):
    if ile==1:
        return a
    return a*iloczyn(a+r,r,ile-1)
print(iloczyn(3,4,7))
print(iloczyn())