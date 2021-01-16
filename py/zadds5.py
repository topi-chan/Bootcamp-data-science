#Napisz funkcję, która zwróci które urodziny będą obchodziły w tym roku osoby
#urodzone w latach podanych w liście będącej argumentem wejściowym danej funkcji.
def birthdate(bd_list):
    for bd in bd_list:
        year = 2021 - bd
        yield year

birth = birthdate([1998, 1987])
for i in birth:
    print(i)
