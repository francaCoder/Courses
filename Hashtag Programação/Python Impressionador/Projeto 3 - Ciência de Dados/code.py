"""
Fazer uma previsão de preço para pessoas no Airbnb, tanto para eu alugar minha casa ou para eu fazer um aluguel
"""

meses = {"jan": 1, "fev": 2,
         "mar": 3, "abr": 4,
         "mai": 5, "jun": 6,
         "jul": 7, "ago": 8,
         "set": 9, "out": 10,
         "nov": 11, "dez": 12}

# Importando Bibliotecas
import pandas as pd
import pathlib

caminho_bases = pathlib.Path("Dataset")

base_airbnb = pd.DataFrame()

for file in caminho_bases.iterdir():
    if file.name[:3] != "tot":
        mes = meses[file.name[:3]]
        ano = int(file.name[-8:].replace(".csv", ""))

    df = pd.read_csv(caminho_bases / file.name)
    df['ano'] = ano
    df['mes'] = mes

    base_airbnb = base_airbnb.append(df)

print(base_airbnb.info())

# base_airbnb.head(1000).to_csv("primeiros_registros.csv", sep=';')


# -- Como temos muitas colunas, nosso modelo pode ficando lento, e com uma análise rápida, podemos ver que várias colunas não são necessárias para o nosso modelo de previsão, por isso vamos excluir algumas colunas da nossa base.
#
# Tipo de colunas que vamos excluir:
# 1 - Ids Links
# 2 - Colunas repetidas ou extremamente parecidas
# 3 - Colunas preenchidas com texto livre. Não rodaremos nenhuma análise de palavras
# 4 - colunas em que todos os valores são iguais

# Vou criar um arquivo em excel com as primeiras 1000 linhas da minha tabela, pra ficar mais fácil e para vermos todas as colunas

colunas = ["host_response_time", "host_response_rate", "host_is_superhost", "host_listings_count", "latitude", "longitude", "property_type", "room_type", "accommodates", "bathrooms", "bedrooms", "beds", "bed_type", "amenities", "price", "security_deposit", "cleaning_fee", "guests_included", "extra_people", "minimum_nights", "maximum_nights", "number_of_reviews", "review_scores_rating", "review_scores_accuracy", "review_scores_cleanliness", "review_scores_checkin", "review_scores_communication", "review_scores_location", "review_scores_value", "instant_bookable", "is_business_travel_ready", "cancellation_policy", "ano", "mes"]

base_airbnb = base_airbnb.loc[:, colunas]
base_airbnb.to_csv("planilha_trabalho.csv")

# Tratar valores faltantes
