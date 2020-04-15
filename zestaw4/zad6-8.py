class Slowa():
    slowo1="aba"
    slowo2="bab"

    
    def __init__(self,a,b):
        self.slowo1=a
        self.slowo2=b

    def czy_palindrom(self):
        print(self.slowo1, )
        if self.slowo1!=self.slowo1[::-1]:
            print("nie ",end="")
        print("jest palindromem.")
        print(self.slowo2, )
        if self.slowo2!=self.slowo2[::-1]:
            print("nie ",end="")
        print("jest palindromem.")

    def czy_metagram(self):
        czy=False
        if len(self.slowo1)==len(self.slowo2):
            Npl=0
            for i in range(len(self.slowo1)):
                if self.slowo1[i]!=self.slowo2[i]:
                    Npl+=1
            if Npl==1:
                czy=True
        if czy:
            print("są to metagramy")
        else:
            print("nie są to metagramy")

    def czy_anagram(self):
        czy=True
        if len(self.slowo1)==len(self.slowo2):
            napis = self.slowo2
            for znak in self.slowo1:
                if znak in napis:
                    i = napis.index(znak)
                    napis = napis[:i]+napis[i+1:]
                else:
                    czy=False
        else:
            czy=False
        if czy:
            print("Są to anagramy")
        else:
            print("nie są to anagramy")   
            

    def wyswietl_wyrazy(self):
        print(self.slowo1)
        print(self.slowo2)

    
    def del(self):
        del self.slowo1
        del self.slowo2


Czy=Slowa("darad","sabaka")
Czy.wyswietl_wyrazy()
Czy.czy_palindrom()
Czy=Slowa("tata","krata")
Czy.czy_metagram()
Czy=Slowa("tata","mata")
Czy.czy_metagram()
Czy=Slowa("tata","karakan")
Czy.czy_metagram()
Czy=Slowa("arbuz","zubra")
Czy.czy_anagram()
Czy=Slowa("tama","krata")
Czy.czy_anagram()
Czy=Slowa("tama","mataa")
Czy.czy_anagram()