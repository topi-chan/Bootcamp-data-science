#Wybierz kilka państw i stwórz dla każdego słownik, który będzie zawierać dane
#o nazwie państwa, powierzchni, liczbie mieszkańców, PKB per capita (PPP).
#Napisz funkcję, która dla listy słowników będzie wypisywać listę państw
#uszeregowanych według: * powierzchni * liczby ludności * gęstości zaludnienia
# * PKB per capita (PPP)
Utopia = {"nazwa":"Utopia", "powierzchnia":"3000", "ludność": "3000","PKB":"4005"}
Dystopia = {"nazwa":"Dystopia", "powierzchnia":"5000", "ludność": "4000","PKB":"100"}
Entropia = {"nazwa":"Entropia", "powierzchnia":"2", "ludność": "10","PKB":"1"}
Anarchia = {"nazwa":"Anarchia", "powierzchnia":"439753", "ludność": "3300","PKB":"3478"}

def sort_country(country_list):
    countries = []
    top_area = []
    top_population = []
    top_PPP = []
    for country in country_list:
        iterator = iter(country.values())
        countries.append(next(iterator))
        top_area.append(int(next(iterator)))
        top_population.append(int(next(iterator)))
        top_PPP.append(int(next(iterator)))
        if hasattr(iterator,'__reversed__'):
            top_area.append(int(next(iterator)))
    countries2 = countries
    countries3 = countries
    countries4 = countries
    top_ppl = [i / j for i, j in zip(top_population, top_area)]
    top_ppl, countries4 = zip(*sorted(zip(top_ppl, countries4)))
    top_population, countries3 = zip(*sorted(zip(top_population, countries3)))
    top_PPP, countries2 = zip(*sorted(zip(top_PPP, countries2)))
    top_area, countries = zip(*sorted(zip(top_area, countries)))
    xx = dict(zip(countries,top_area))
    print("Powierzchnia:")
    for k,v in xx.items():
        print(k,":",v)
    xx = dict(zip(countries3,top_population))
    print("Liczba ludności:")
    for k,v in xx.items():
        print(k,":",v)
    xx = dict(zip(countries4,top_ppl))
    print("Gęstość zaludnienia:")
    for k,v in xx.items():
        print(k,":",v)
    xx = dict(zip(countries2,top_PPP))
    print("PKB:")
    for k,v in xx.items():
        print(k,":",v)


sort_country([Utopia,Dystopia,Entropia,Anarchia])
