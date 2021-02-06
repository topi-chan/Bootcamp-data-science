from pd3 import *
exp = []
for e in df['doświadczenie']:
    if e <= 3:
        exp.append("junior")
    if (e > 3 and e <= 8):
        exp.append("mid")
    if (e > 8 and e <= 12):
        exp.append("senior")
    if e > 12:
        exp.append("expert")
df['doświadczenie'] = exp
