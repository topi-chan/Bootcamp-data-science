import pandas as pd
df = pd.read_csv('dataset_pandas_pd.csv', delimiter=',', names = ['imię',
    'nazwisko', 'rok_urodzenia', 'miesiąc_urodzenia', 'dzień_urodzenia',
    'miejsce_urodzenia', 'oddział', 'departament', 'rozpoczęcie_rok',
    'rozpoczęcie_miesiąc', 'rozpoczęcie_dzień', 'doświadczenie'])
gender = []
for n in df.nazwisko:
    if n.endswith('i'):
        gender.append("mężczyzna")
    else:
        gender.append("kobieta")
df['płeć'] = gender
