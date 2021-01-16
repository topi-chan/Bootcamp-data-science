#Napisz funkcję o dwóch argumentach, która sprawdzi, czy jedna liczba
#jest podzielna przez drugą liczbę.

def divisible(a, b):
    if a % b == 0:
        print("Podzielna")
    else:
        print("Niepodzielna")

divisible(4,3)
