# Head function returns the first 5 rows for the object basede on position.
# Tail function is used to view last 5 rows of a Dataframe.
import pandas as pd

DataFrame = pd.read_csv('hello.csv')
FirstColumn = 5
lastColumn = 5
print(DataFrame.head(FirstColumn)) # 
print(DataFrame.tail(lastColumn))














