# 08. Renomeie as colunas do seguinte DataFrame para português.
import pandas as pd

df = pd.DataFrame({
    "Name": ["Ana", "Carlos", "Beatriz"],
    "Age": [15, 22, 17],
    "Sex": ["female", "male", "female"]
})

df.rename(columns={'Name': 'Nome', 'Age': 'Idade', 'Sex': 'Sexo'}, inplace=True)

print(df)
