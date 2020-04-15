class arytmetyczne():
    a1=0
    r=0
    ile=0

    def wyswietl_dane(self):
        print("Pierwszy wyraz ciagu: ",self.a1)
        print("Roznica: ", self.r)
        print("Ilosc: ", self.ile)

    def pobierz_elementy(self, a, b):
        self.a1=a
        self.r=b

    def pobierz_parametry(self, a, b, c):
        self.a1=a
        self.r=b
        self.ile=c
        return self.a1+self.r*(self.ile-1)

    def policz_sume(self):
        return ((self.a1+(self.a1+self.r*(self.ile-1)))/2)*self.ile

    def policz_elementy(self):
        for i in range(self.ile):
            print("a_",i+1,": ",self.a1+self.r*(i),sep="")
    
AA=arytmetyczne()
AA.wyswietl_dane()
AA.pobierz_elementy(4,6)
AA.wyswietl_dane()
print(AA.pobierz_parametry(4,8,2))
AA.wyswietl_dane()
print(AA.policz_sume())
AA.policz_elementy()