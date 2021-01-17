# Stwórz klasę reprezentującą linię prostą, która przyjmuje w konstruktorze
# współrzędne obu końców w układzie współrzędnych XY. Klasa implementuje metodę
# obliczającą długość linii.
from math import sqrt

class StraightLine():

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def calculate(self):
        return sqrt(((self.x2-self.x1)**2)+((self.y2-self.y1)**2))

obj = StraightLine(1,-4,2,3)
print(obj.calculate())
