import pandas as pd
df = pd.read_csv("imppat.csv")
df
df1 = df['IMPPAT Phytochemical identifier']
df1
df1.to_excel('IMPPAT Phytochemical identifier.xlsx')
