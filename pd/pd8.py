from pd6 import *
d = df[df['doświadczenie'] == "senior"].groupby('oddział').count()
print(d['doświadczenie'].idxmax(axis=0))
