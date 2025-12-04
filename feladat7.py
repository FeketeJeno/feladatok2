#OOP: Egyszerű Osztály – Auto


class Auto:
    def __init__(self, marka, tipus, evjarat):
        self.Marka = marka
        self.Tipus = tipus
        self.Evjarat = evjarat

    def kiir(self):
        print(f"{self.Marka},{self.Tipus}, {self.Evjarat}")

auto1 = Auto("Audi","A4",2022)
auto2 = Auto("BMW","I3",2024)


auto2.kiir()