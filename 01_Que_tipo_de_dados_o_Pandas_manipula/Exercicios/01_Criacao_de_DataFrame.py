# 01. Crie um DataFrame que contenha as colunas Nome,
# Idade e Cidade com pelo menos 3 registros fictícios.

import pandas as pd

df = pd.DataFrame(
    {
         "Nome": [
            "Matheus Parreira",
            "João Armonia",
            "Gabriel Amorin",
       ],
        "Idade": [34, 45, 24],
        "Cidade": ["Rio de Janeiro", "Belo Horizonte", "Januária"],
    }
)

print(df)
