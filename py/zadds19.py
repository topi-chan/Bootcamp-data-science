#Zaimplementuj klasę bazową Figura. Klasa będzie mieć metody obliczające pole i
#obwod. Stwórz klasy reprezentujące trójkąt i prostokąt, implementujące
#odpowiednio obie metody.
class Figura():
    """klasa bazowa; wartosc1 = podstawa trojkata lub bok prostokata;
    wartosc2 = wysokosc trojkata lub drugi bok prostokata;
    args = faktultatywnie dodatkowe boki trójkąta"""

    def __init__(self, wartosc1, wartosc2, *args):
        self.wartosc1 = wartosc1
        self.wartosc2 = wartosc2
        self.args = args
        self.wynik_pole = 0
        self.wynik_obwod = 0


    def calculate_geometry(self):
        self.wynik_pole = self.wartosc1 * self.wartosc2


class Prostokat(Figura):
    """dziedziczy wynik z Figury"""

    def calculate_rectangle(self):
        return self.wynik_pole


class Trojkat(Figura):
    """dziedziczy wynik z Figury, dzieli przez 2 bo to trójkąt ;)"""

    def calculate_triangle(self):
        return (self.wynik_pole/2)


obj = Figura(19,12)
print(Prostokat().calculate_rectangle())
print(obj2.calculate_rectangle())
