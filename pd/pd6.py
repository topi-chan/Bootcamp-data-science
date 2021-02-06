from pd5 import *

mid = df.loc[df['doświadczenie'] == "mid"].mean()
senior = df.loc[df['doświadczenie'] == "senior"].mean()
expert = df.loc[df['doświadczenie'] == "expert"].mean()

exp_lvl = {"mid":int(mid.rozpoczęcie_rok), "senior":int(senior.rozpoczęcie_rok),
    "expert":int(expert.rozpoczęcie_rok)}
df['rozpoczęcie_rok'] = df['doświadczenie'].map(exp_lvl)
