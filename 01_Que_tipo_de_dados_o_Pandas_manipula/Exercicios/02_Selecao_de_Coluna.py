# 02. No DataFrame abaixo, selecione apenas a coluna Sex e exiba seu conteúdo.

import pandas as pd

df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "Sex": ["female", "male", "male"]
})

print(df["Sex"])
