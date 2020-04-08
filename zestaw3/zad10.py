def lista_rzeczy(**rzeczy):
    print("Lista zakupow:\n")
    ile=0
    for a in rzeczy:
        ile+=rzeczy[a]
    print("\nIlosc produktow w sumie:",ile)
lista_rzeczy(papier=25,mleko=4,pomarancze=8,banany=9)