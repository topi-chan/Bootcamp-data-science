from pd6 import *
d = df[(df['doświadczenie'] == "senior")
    & (df['rozpoczęcie_rok'] > 2010)].groupby('oddział').count()
print(d)
