# 03. Com base no DataFrame criado no exercício 1, calcule a média das idades.

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

media_idades = df["Idade"].mean()

print("Média das idades: {:.2f}".format(media_idades))
