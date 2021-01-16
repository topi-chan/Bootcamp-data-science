#Napisz funkcję przyjmującą jeden parametr list zawierający liczby całkowite i
#zwracającą element, który pojawia się na liście najczęściej.

def most_common(num_list):
    if (isinstance(num_list, list)) and (all(isinstance(x, int)
        for x in num_list)) is False:
        print("Proszę podać listę zawierającą liczby całkowite")
        quit()
    return max(set(num_list), key=num_list.count)

print(most_common([0,2,2,2,3,4,3]))
