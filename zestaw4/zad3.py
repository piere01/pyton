with open("zad3.txt", "w+") as plik:
    plik.write("To jest pierwsza linijka tekstu\n")
    plik.write("A to jest druga a także ostatnia linijka tekstu\n")
    plik.seek(0,0)
    for linia in plik:
        print(linia, end="")