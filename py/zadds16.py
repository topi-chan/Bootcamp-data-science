# Stwórz klasę Pamiętnik, która zaimplementuje metody do odczytywania i
# dopisywania zawartości. Zawartość będzie przechowywana w pliku tekstowym.
from sys import argv

class Pamietnik():
    """odczytuje i dopisuje string do pliku"""

    def __init__(self, fname):
        self.lista = []
        self.fname = fname

    def read(self):
        fname = open(self.fname)
        while True:
            fh = fname.readline().strip()
            print(fh)
            if fh == "": self.write()

    def write(self):
        while True:
            dopisz = input("Co chcesz dopisać? (pusta linijka przerywa program)")
            self.lista.append(dopisz)
            if dopisz == "": self.save()

    def save(self):
        fd = open(self.fname, "w")
        for element in self.lista:
            fd.write(str(element))
            fd.write("\n")
        quit()

obj = Pamietnik(argv[1])
obj.read()
