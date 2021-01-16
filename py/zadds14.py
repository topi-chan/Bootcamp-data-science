#Napisz (przy pomocy rekurencji) funkcję realizującą potęgowanie. Funkcja
#przyjmuje dwie liczby całkowite, będące podstawą i wykładnikiem potęgi.
def power(func):
    def decorator(a, b):
        return func(a,b)**b
    return decorator

@power
def numbers(a, b):
    if (isinstance(a, int)) and (isinstance(b, int)) is True:
        pass
    else:
        print("Proszę podać dwie liczby całkowite jako argumenty funkcji")
        quit()
    return a

print(numbers(3, 4))
