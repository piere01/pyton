plik=open("zad1.txt","w+")
[plik.write(str(x)+" ") for x in range(1,255) if x%4==0]
plik.close()