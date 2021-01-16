#Napisz funkcję, która przyjmie słownik mapujący imiona na wzrost, a następnie
#zwróci listę zawierającą imiona posortowane według wzrostu malejąco.
from zadds12 import person

def sort_by_height(dictionary_given):
    persons_sorted = dict(sorted(dictionary_given.items(),
        reverse = True, key=lambda item: item[1]))
    return list(persons_sorted.keys())
print(sort_by_height(person))
