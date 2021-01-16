#Utworz funkcję, która przyjmie argument int n i obliczy n-ta
#liczbę ciagu Fibonacciego.
def fibonacci(n):
    if (isinstance(n, int)) is False:
        print("Proszę podać liczbę")
        quit()
    if n<=0:
        print("Liczba musi być większa od 0")
        quit()
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(21))
