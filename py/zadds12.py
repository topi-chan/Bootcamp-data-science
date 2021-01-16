#Napisz funkcję, która przyjmie argumenty nazwane imie i wzrost a następnie
#utworzy wpis do globalnego słownika. Dodaj co najmniej 5 wpisów.
person = {}
def define_person(**kwargs):
    global person
    for imie, wzrost in kwargs.items():
        person.update({imie: wzrost})

define_person(Kasia = 180, Maciek = 190, Ola=160, Magda=155, Wojtek=185)
if __name__ == "__main__":print(person)
