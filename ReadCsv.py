import pandas as pd

DataFrame = pd.read_csv('hello.csv')
FirstColumn = 5
lastColumn = 5
print(DataFrame.head(FirstColumn))
print(DataFrame.head(lastColumn))