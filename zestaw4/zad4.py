class NaZakupy():
    nazwa_produktu=""
    ilosc=0
    jednostka_miary=""
    cena=0

    def __init__(self, a, b, c, d):
        self.nazwa_produktu=a
        self.ilosc=b
        self.jednostka_miary=c
        self.cena=d

    def wyswietl_produkt(self):
        print("Nazwa produktu: ",self.nazwa_produktu)
        print("Ilosc: ",self.ilosc)
        print("Jednostka miary: ",self.jednostka_miary)
        print("Cena jednostkowa: ",self.cena)

    def ile_produktu(self):
        print(self.ilosc, self.jednostka_miary)

    def ile_kosztuje(self):
        print(self.ilosc*self.cena)

AA=NaZakupy("makaron",5,"kg",2.99)
AA.wyswietl_produkt()
AA.ile_produktu()
AA.ile_kosztuje()