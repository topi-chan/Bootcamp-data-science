from pd6 import *
d = df[(df['doświadczenie'] == "mid")
    & (df['rok_urodzenia'] < 1975)
    & (df['płeć'] == "kobieta")].groupby('oddział').count()
print(d)
