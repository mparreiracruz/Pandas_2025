# 07. Adicione uma nova coluna chamada Categoria ao DataFrame abaixo.
# A categoria será "Adulto" para pessoas com idade maior ou igual a 18 e "Menor" caso contrário.

import pandas as pd

df = pd.DataFrame({
    "Name": ["Ana", "Carlos", "Beatriz"],
    "Age": [15, 22, 17]
})

df['Categoria'] = df['Age'].apply(lambda x: 'Adulto' if x >= 18 else 'Menor')

print(df)


