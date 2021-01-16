#Napisz funkcję przyjmujacą napis i zwracającą
#informacje ile liter i cyfr jest w napisie.
def informer(a):
    countl = 0
    countn = 0
    counto = 0
    for i in a:
        if i.isalpha():
            countl += 1
        elif i.isdigit():
            countn += 1
        else:
            counto += 1
    print("Liczba liter to:", countl)
    print("Liczb jest:", countn)
    print("Liczba znaków specjalnych to:", counto)

informer("dsjdskjds 9898 d")
