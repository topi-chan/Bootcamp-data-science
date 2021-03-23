import pandas as pd

df = pd.read_csv('dataset_pandas_pd.csv', delimiter=',', names = ['imię',
    'nazwisko', 'rok_urodzenia', 'miesiąc_urodzenia', 'dzień_urodzenia',
    'miejsce_urodzenia', 'oddział', 'departament', 'rozpoczęcie_rok',
    'rozpoczęcie_miesiąc', 'rozpoczęcie_dzień', 'doświadczenie'])
print(df['nazwisko'].value_counts().idxmax())

#alternative methods:
# print(df.sort_values(by='nazwisko'))
# print(df.groupby('nazwisko').count())
