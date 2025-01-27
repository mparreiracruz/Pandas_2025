import pandas as pd
titanic = pd.read_csv("Titanic.csv")

print(titanic)

print(titanic.head(8))# Quero ver as primeiras 8 linhas de um DataFrame do pandas.

print(titanic.tail(8))# Quero ver as últimas 8 linhas de um DataFrame do pandas.

print(titanic.dtypes)# Os tipos de dado aqui DataFrame são inteiros ( int64), flutuantes ( float64) e strings ( object).

titanic.to_excel("Titanic.xlsx", sheet_name="passengers", index=False)

print(titanic.info())