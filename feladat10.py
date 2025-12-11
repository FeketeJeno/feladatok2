"""
OOP: Öröklődés

Készíts egy Allat alaposztályt (név, életkor).
Készíts két leszármazottat:

Kutya (plusz: fajta)

Macska (plusz: szín)

Mindkettőnek legyen hang() metódusa, ami kiírja a saját hangját.
Példányosítsd őket és hívd meg a metódust."""

class Allat:
    def __init__(self, nev,eletkor):
        self.name = nev
        self.age = eletkor

class Kutya(Allat):
    def __init__(self, nev, eletkor, fajta):
        super().__init__(nev,eletkor)
        self.type = fajta
    def hang(self):
        print("Vau")


class Macska(Allat):
    def __init__(self, nev, eletkor, szin):
        super().__init__(nev, eletkor) #öröklés
        self.color = szin

    def hang(self):
        print("Miau")


kutya = Kutya("Bodri", 10, "Labradore")
kutya.hang()

macska = Macska("Cirmos", 8, "Házi")
macska.hang()



    


