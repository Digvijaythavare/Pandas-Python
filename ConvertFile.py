import pandas as pd

DataFrame = pd.read_csv('hello.csv')
DataFrame.to_excel('ExcelFile.xlsx', index=False)