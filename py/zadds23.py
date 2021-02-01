# Stwórz klasy potomne dla klasy bazowej zwierzęcia, reprezentujące psa i kota.
# W konstruktorze każdej z nich ustaw odpowiednio zmienną reprezentującą typ
# zwierzęcia. Zaimplementuj odpowiednio metodę daj_głos w każdej z klas potomnych.
# Sprawdź, czy obiekty stworzone z klas Pies i Kot potrafią poprawnie się przywitać.
from zadds22 import Zwierze


class Pies(Zwierze):

    def __init__(self, imie):
        self.typ_zwierzecia = type(self)
        self.imie = imie

class Kot(Zwierze):

    def __init__(self, imie):
        self.typ_zwierzecia = type(self)
        self.imie = imie


burek = Pies("Burek")
tazik = Kot("Tazior")
burek.daj_glos("woofwoof")
tazik.daj_glos("meow")
burek.powitanie()
tazik.powitanie()
