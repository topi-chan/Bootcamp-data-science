from pd6 import *
d = df[df['departament'] == "Data Science"].groupby('oddział').count()
d['departament'].idxmax(axis=0)
