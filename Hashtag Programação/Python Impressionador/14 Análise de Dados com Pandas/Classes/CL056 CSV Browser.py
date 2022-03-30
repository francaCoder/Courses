import pandas as pd

url = "https://drive.google.com/uc?authuser=0&id=1UzlPy6CZQeAzDXhfc_2sHEyK_Jb50vJs&export=download"
money = pd.read_csv(url)
print(money)
