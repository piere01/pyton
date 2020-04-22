class Material():
    rodzaj=""
    dlugosc=0
    szerokosc=0

    def __init__(self,a,b,c):
        self.rodzaj=a
        self.dlugosc=b
        self.szerokosc=c
    def nazwa(self):
        print(self.__class__.__name__)


class Ubranie(Material):
    rozmiar=""
    kolor=""
    dla_kogo=""

    def wyswietl_dane(self):
        print("{} {} {} {} {} {}".format(self.rodzaj, self.dlugosc, self.szerokosc, self.rozmiar, self.kolor, self.dla_kogo))


class bluza(Ubranie):
    rodzaj_bluzy=""

    def wyswietl_dane(self):
        print("{} {} {} {} {} {} {}".format(self.rodzaj, self.dlugosc, self.szerokosc, self.rozmiar, self.kolor, self.dla_kogo, self.rodzaj_bluzy))


bawelna=Material("naturalna",28,62)
bawelna.nazwa()
Koszula=Ubranie("naturalny",47,25)
Koszula.rozmiar="L"
Koszula.kolor="biala"
Koszula.dla_kogo="Zygmunt"
Koszula.wyswietl_dane()
Koszula.nazwa()
bluza=bluza("bawelna",55,52)
bluza.rodzaj_bluzy="na suwak"
bluza.kolor="Żółty"
bluza.rozmiar="XL"
bluza.dla_kogo="Edyp"
bluza.wyswietl_dane()
bluza.nazwa()