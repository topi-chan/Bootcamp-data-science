#Stwórz klasę przyjmującą w konstruktorze listę będącą kolejnymi wierszami
#piosenki. Klasa będzie mieć metodę spiewaj, która wypisze wszystkie wiersze
#piosenki po kolei.
class Song():

    def __init__(self, song_list):
        self.song_list = song_list

    def spiewaj(self):
        for verse in self.song_list:
            print(verse)

obj = Song(["lala","tata","ma","kota"])
obj.spiewaj()
