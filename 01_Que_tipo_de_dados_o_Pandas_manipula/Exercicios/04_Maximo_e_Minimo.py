#04. Crie um DataFrame com uma coluna chamada Notas
# contendo os valores [78, 95, 62, 88, 70].
# Exiba a maior e a menor nota.

import pandas as pd

df = pd.DataFrame({
    "Notas": [78, 95, 62, 88, 70]})

print(df)

maior_nota = df["Notas"].max()
menor_nota = df["Notas"].min()

print("Maior nota: ", maior_nota)
print("Menor nota: ", menor_nota)