import pandas as pd

df = pd.read_csv('/home/leia/mycode/amazon-orders.csv')

df = df.fillna(0)
df["Total Charged"] = df["Total Charged"].str.replace('$','').astype(float)


print(df["Total Charged"].sum())