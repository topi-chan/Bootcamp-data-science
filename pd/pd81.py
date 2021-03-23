from pd6 import *

mapping = {'Software Development':'Software Development Team',
'HR':'Human Resources','Data Science':'Data Analytics'}
df['departament'] = df['departament'].map(mapping)
print(df['departament'])

#example for column names:
# df.rename(columns={"Software Development":"Software Development Team",
#             "HR":"Human Resources", "Data Science":"Data Analytics"})
