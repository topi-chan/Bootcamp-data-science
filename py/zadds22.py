# Stwórz abstrakcyjną klasę bazową reprezentującą zwierzę. Konstruktor klasy
# będzie przyjmować parametr reprezentujący imię zwierzęcia. Klasa będzie mieć 2
# metody. Jedna metoda daj_glos będzie abstrakcyjna. Druga metoda powitanie będzie
# wyświetlać napis, składający się z wartości zwracanej przez daj_glos,
# z wyświetlenia imienia zwierzęcia oraz z wyświetlenia jakiego typu (atrybut typ
# dla klasy) jest zwierzę.
from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def daj_glos():
        pass


class Zwierze(Animal):

    def __init__(self, imie):
        self.imie = imie
        self.dzwiek = None

    def daj_glos(self, dzwiek):
        self.dzwiek = dzwiek

    def powitanie(self):
        print(self.dzwiek, self.imie, type(self))

if __name__ == '__main__':
    atanazy = Zwierze("Tazik")
    atanazy.daj_glos("miauu")
    atanazy.powitanie()
