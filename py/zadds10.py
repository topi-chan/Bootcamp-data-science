# Napisz funkcję, która przyjmie dwie listy liczb całkowitych, i zwróci listę
# liczb występujących w pierwszej i nie występujących w drugiej liście,
# posortowana rosnąco względem ilości wystąpień w pierwszej liście.

def lists_difference(list1,list2):
    if (isinstance(list1, list)) and (isinstance(list2, list)) is False:
        print("Proszę podać dwie listy jako argumenty funkcji")
        quit()
    if (all(isinstance(x, int) for x in list1) and all(isinstance(x, int)
        for x in list2)) is False:
            print("Podano znaki nie będące liczbą całkowitą")
            quit()
    list0 = list(set(list1) - set(list2))
    for m in list0:
        for n in list1:
            if n not in list0:
                list1.remove(n)
    list1_ordered = sorted(list1, key = list1.count)
    return list1_ordered


print(lists_difference([12,2,2,5,6,6,7,4,12,12,4,12,5,4,4],[1,2,5,12]))
