#Napisz funkcję, która dla dwóch list liczbowych zwróci listę zawierającą
#tylko te elementy, które należą do obydwu list wejściowych.

def get_common(a,b):
    return list(set(a).intersection(b))

print(get_common([2,3,4,6,7,2,3],[3,5,7,9,4,2]))
