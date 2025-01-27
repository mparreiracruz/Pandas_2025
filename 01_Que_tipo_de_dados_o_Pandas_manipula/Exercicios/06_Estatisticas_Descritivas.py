# 06. Crie um DataFrame contendo 10 registros com
# as colunas Altura e Peso. Use números aleatórios para os valores.
# Utilize o método .describe() para obter estatísticas descritivas.

import pandas as pd

df = pd.DataFrame({
    "Altura": [1.70, 1.65, 1.80, 1.75, 1.90, 1.60, 1.85, 1.73, 1.68, 1.77],
    "Peso": [70.5, 60.3, 85.0, 78.2, 90.1, 55.0, 88.4, 74.3, 66.2, 80.0]
})

print(df.describe())