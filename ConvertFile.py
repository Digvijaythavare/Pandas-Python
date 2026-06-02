import pandas as pd

df = pd.read_csv("hello.csv")
df.to_excel("practice_extended.xlsx", index=False)

