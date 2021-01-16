#Stwórz klasę Trójkat, w której konstruktor przyjmuje 3 argumenty,
#reprezentujące kąty trójkąta. Klasa implementuje metodę sprawdz_katy, która
#sprawdzi, czy suma kątow jest równa 180.
class Trojkat():

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.suma = 0

    def sprawdz_katy(self):
        self.suma = (self.a+self.b+self.c)
        if self.suma == 180:
            print("Suma kątów to 180 stopni")
            return False
        else:
            print("Suma kątów nie równa się 180 stopni")
            return True

obj = Trojkat(60,60,60)
obj.sprawdz_katy()
