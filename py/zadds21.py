# Stwórz klasę reprezentującą wielokąt i przyjmującą w konstruktorze listę
# kolejnych linii (obiekty klasy z poprzedniego zadania), reprezentujących kolejne
# boki wielokąta. Klasa powinna sprawdzić, czy dane są poprawne (czy każda linia
# kończy się tam, gdzie zaczyna następna). Klasa wielokąta implementuje również
# metodę obliczającą obwód.
from math import sqrt

class StraightLine():

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def calculate(self):
        return sqrt(((self.x2-self.x1)**2)+((self.y2-self.y1)**2))

obj = StraightLine(1,4,2,3)
obj1 = StraightLine(2,4,5,2)
obj2 = StraightLine(6,3,4,2)
obj3 = StraightLine(3,4,5,2)
obj4 = StraightLine(4,4,4,3)
obj5 = StraightLine(6,4,4,2)


class Polygon():

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def calculate_circuit(self):
        return sum(self.__dict__.values())

pol = Polygon(l = obj.calculate(), l1 = obj1.calculate(), l2 = obj2.calculate(),
    l3 = obj3.calculate(), l4 = obj4.calculate(), l5 = obj5.calculate())

print(pol.calculate_circuit())
