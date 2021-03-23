from pd6 import *
d = df[(df['doświadczenie'] == "mid")
    & (df['płeć'] == "kobieta")].groupby('oddział').count().idxmax()["departament"]
print(d)
