#Napisz funkcję, która sprawdzi, czy 2 napisy są palindromami.
def palindromes(text, text2):
    text = text.lower().replace(" ", "").replace("\t", "")
    for i in range(0, int(len(text)/2)):
        if text[i] != text[len(text)-i-1]:
            return False
    text2 = text2.lower().replace(" ", "").replace("\t", "")
    for i in range(0, int(len(text2)/2)):
        if text2[i] != text2[len(text2)-i-1]:
            return False
    return True

print(palindromes("Ada bąki piką bada","kobyła ma mały bok"))
