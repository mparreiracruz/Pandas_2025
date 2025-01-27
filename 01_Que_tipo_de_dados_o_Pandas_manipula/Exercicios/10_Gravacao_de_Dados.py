# 10. Crie um DataFrame com informações fictícias e
# salve-o em um arquivo CSV chamado dados.csv.
# Depois, carregue o arquivo de volta para um novo DataFrame
# e exiba seu conteúdo.

import pandas as pd

df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "Diana"],
    "Age": [25, 30, 35, 40],
    "Sex": ["female", "male", "male", "female"]
})

df.to_csv('dados.csv', index=False)

# Carregando o arquivo CSV de volta para um novo DataFrame
df_loaded = pd.read_csv("dados.csv")

# Exibindo o conteúdo do DataFrame carregado
print(df_loaded)
