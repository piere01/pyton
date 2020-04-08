def rownolegle_czy_prostopadle(a,b,c,d):
    if a==c:
        print("Rownolegle")
    elif a*c==-1:
        print("Prostopadle")
    else:
        print("zadne z powyzszych")
e=int(input('Podaj a: '))
f=int(input('Podaj b: '))
g=int(input('Podaj c: '))
h=int(input('Podaj d: '))
rownolegle_czy_prostopadle(e,f,g,h)