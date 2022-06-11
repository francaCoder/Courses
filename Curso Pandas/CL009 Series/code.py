import pandas as pd

teste = pd.Series([1, 63, 55, 88])
print(teste)
# 0     1
# 1    63
# 2    55
# 3    88
# dtype: int64
print()

teste2 = pd.Series([1, 2, 3, 4.7])
print(teste2) # Converteu toda a coluna para flutuante
# 0    1.0
# 1    2.0
# 2    3.0
# 3    4.7
# dtype: float64
print()

teste3 = pd.Series([1, 2.4, 3, "4.6"])
print(teste3)
# 0      1
# 1    2.4
# 2      3
# 3    4.6
# dtype: object
print()

s = pd.Series({"a": 12, "b": 90, "c": 123})

# posso acessar ele como se fosse uma lista
# ou passando as chaves dentro de um array também
