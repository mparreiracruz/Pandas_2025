# 06. Crie um DataFrame contendo 10 registros com
# as colunas Altura e Peso. Use números aleatórios para os valores.
# Utilize o método .describe() para obter estatísticas descritivas.

import pandas as pd
import numpy as np

# Criando o DataFrame com valores aleatórios
np.random.seed(42)  # Para reprodutibilidade
df = pd.DataFrame({
    "Altura": np.random.uniform(1.5, 2.0, 10),  # Alturas entre 1.5m e 2.0m
    "Peso": np.random.uniform(50, 100, 10)      # Pesos entre 50kg e 100kg
})

# Estatísticas descritivas
print(df.describe())

