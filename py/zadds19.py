#Zaimplementuj klasę bazową Figura. Klasa będzie mieć metody obliczające pole i
#obwod. Stwórz klasy reprezentujące trójkąt i prostokąt, implementujące
#odpowiednio obie metody.
class Figura():
    """klasa bazowa; wartosc1 = podstawa trojkata lub bok prostokata;
    wartosc2 = wysokosc trojkata lub drugi bok prostokata;
    wartosc3 = trzeci bok trójkąta"""

    def __init__(self, wartosc1, wartosc2, wartosc3):
        self.wartosc1 = wartosc1
        self.wartosc2 = wartosc2
        self.wartosc3 = wartosc3
        self.wynik_pole = 0
        self.wynik_obwod = 0

    def calculate_geometry(self):
        self.wynik_pole = self.wartosc1 * self.wartosc2
        self.wynik_obwod = self.wartosc1 + self.wartosc2 + self.wartosc3

class Prostokat(Figura):
    """dziedziczy wynik z Figury"""

    def __init__(self, *args, **kwargs):
        if 'obj' in kwargs:
            self.__dict__.update(kwargs['obj'].__dict__)
        else:
            super().__init__(*args, **kwargs)


    def calculate_rectangle(self):
        return self.wynik_pole

    def calculate_circuit(self):
        return (self.wartosc1*2 + self.wartosc2*2)
        

class Trojkat(Figura):
    """dziedziczy wynik z Figury, dzieli przez 2 bo to trójkąt ;)"""

    def calculate_triangle(self):
        return (self.wynik_pole/2)

    def calculate_circuit(self):
        return self.wynik_obwod

objj = Figura(23,23,12)
objj.calculate_geometry()
figurka = Prostokat(obj = objj)
print(figurka.calculate_circuit())
# obj = Prostokat(19,12,2)
# obj.calculate_geometry()
# print(obj.calculate_rectangle())
# print(obj.calculate_circuit())
# obj2 = Trojkat(19,12,2)
# obj2.calculate_geometry()
# print(obj2.calculate_triangle())
# print(obj2.calculate_circuit())
