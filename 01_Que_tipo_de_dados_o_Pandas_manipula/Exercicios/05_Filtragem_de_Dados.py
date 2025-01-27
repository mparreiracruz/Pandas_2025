# 04. Usando o seguinte DataFrame, selecione
# apenas as pessoas com idade maior que 30:
import pandas as pd

df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "Sex": ["female", "male", "male"]
})

pessoas_acima_de_30_anos = df[df["Age"] > 30]

print(pessoas_acima_de_30_anos)
