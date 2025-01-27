# 09. Com o DataFrame abaixo, agrupe os dados
# por Sex e calcule a média de idade de cada grupo:
import pandas as pd

df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "Diana"],
    "Age": [25, 30, 35, 40],
    "Sex": ["female", "male", "male", "female"]
})

agrupar = df.groupby('Sex')['Age'].mean()
# agrupar_por_sexo = df.sort_values('Sex')
print(agrupar)
