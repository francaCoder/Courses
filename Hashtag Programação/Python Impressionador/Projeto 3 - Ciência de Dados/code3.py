import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, ExtraTreesRegressor
from sklearn.model_selection import train_test_split

base_airbnb = pd.read_csv("base_airbnb.csv", sep=',')

# Verificar os tipos de dados de cada coluna, o nosso modelo de previsão trata de forma diferente dependendo do tipo de dado em cada coluna, então temos que tratar


# Como o price e o extra people estão sendo reconhecidos como objeto, ao invés de ser um float, temos que mudar o tipo de dado das colunas

# Price
# Extra People

base_airbnb['price'] = base_airbnb['price'].str.replace("$", "")
base_airbnb['price'] = base_airbnb['price'].str.replace(",", "")

# Mudar o formato, astype, eu quero ver ele como tipo...
# Float32 = mais leve que Float64
base_airbnb['price'] = base_airbnb['price'].astype(np.float64, copy=False)

base_airbnb['extra_people'] = base_airbnb['extra_people'].str.replace("$", "")
base_airbnb['extra_people'] = base_airbnb['extra_people'].str.replace(",", "")
base_airbnb['extra_people'] = base_airbnb['extra_people'].astype(np.float64, copy=False)

# print(base_airbnb.info())
# print(base_airbnb.iloc[0])

# começar a análise exploratória

# Vamos basicamente olhar feature por feature para:
# 1 - Ver a correlação entre as colunas e decidir se manteremos todas as nossas features
# 2 - Excluir os outliers (usaremos como regra, valores abaixo de Q1 -1.5x amplitude e valores acima de Q3 + 1.5x amplitude) amplitude = Q3 - Q1
# 3 - confirmar se realmente todas as features que temos, de fato vai nos ajudar em nosso modelo ou se podemos excluir elas

# Vamos começar pelas colunas de preço (resultado final que queremos) e de extra_people (também valor monetário). Esse são os valores numéricos contínuos.
# Depois vamos analisar as colunas com valores numéricos discretos (acomodações, quartos, guest_include, etc.)
# Por fim vamos analisar as colunas de texto e definir quais categorias fazem sentido mantermos ou não

# 1
# Só printando a base airbnb.corr para vermos a correlação, fica muito ruim de fazer uma análise visual, então vamos fazer um mapa de calor, usando a biblioteca do seaborn
# print(base_airbnb.corr())

plt.figure(figsize=(15, 10))

# Quero que ele me mostre o mapa de calor da correlação das colunas da base airbnb
# annot = padrão, cmap = cor do gráfico

sns.heatmap(base_airbnb.corr(), annot=True, cmap="Reds")

plt.show()


# Vamos deifinir algumas funções para ajudar na análise de outliers das colunas

def limites(coluna):
    # Baseado em cada coluna, a gente vai estabelecer o limite mínimo e o limite máximo
    # Calcular os quartis
    q1 = coluna.quantile(0.25)
    q3 = coluna.quantile(0.75)
    amplitude = q3 - q1

    limite_inferior = q1 - 1.5 * amplitude
    limite_superior = q3 + 1.5 * amplitude

    return limite_inferior, limite_superior


# print(limites(base_airbnb['bedrooms']))

def diagrama_caixa(coluna):
    fig, (ax1, ax2) = plt.subplots(1, 2)
    fig.set_size_inches(15, 5)  # aumentar o tamanho

    sns.boxplot(x=coluna, ax=ax1)  # Primeiro gráfico

    ax2.set_xlim(limites(coluna))  # Esse gráfico vai ser plotado do limite inferior até o limite superior, porque é a resposta da nossa função de limites
    sns.boxplot(x=coluna, ax=ax2)  # Segundo gráfico

    plt.show()


# print(diagrama_caixa(base_airbnb['price']))


def histograma(coluna):
    # Já existe esse gráfico pronto dentro do seaborn
    plt.figure(figsize=(15, 5))
    sns.distplot(coluna, hist=True)
    plt.show()


# print(histograma(base_airbnb['price']))

# Analisando colunas

# Price - diária do local
# gráfico esquerda - a maioria dos valores são bem pequenos mas a gente tem uma série de outliers que vem depois, alguns até gigantescos que chegam a 140 mil
# gráfico direita - se a gente usar a métrica de outlier que a gente definiu, a gente vai pegar os valores entre 0 e 1200 e pouco

# Como tomar a decisão de excluir os outliers ou não?
# Vamos excluir porque locais com esses preços gigantescos não são para pessoas normais, provavelmente são imóveis de luxo e não é o objetivo da nossa base incluir eles

def excluir_outliers(df, nome_coluna):
    # essa função tem que excluir os outliers do df e me dizer quantas linhas foi que ele excluiu, pra sabermos se realmente faz sentido a gente excluir aquele outlier ou não
    qtd_linhas_antiga = base_airbnb.shape[0]  # .shape retorna uma tupla com Linhas X Colunas
    lim_inf, lim_sup = limites(df[nome_coluna])
    df = df.loc[(df[nome_coluna] >= lim_inf) & (df[nome_coluna] <= lim_sup), :]
    # quero as linhas daquela coluna onde são maiores que o limite inferior e menores que o limite superior, assim excluindo os outliers
    linhas_removidas = qtd_linhas_antiga - df.shape[0]
    return df, linhas_removidas


def grafico_barra(coluna):
    plt.figure(figsize=(15, 5))
    ax = sns.barplot(x=coluna.value_counts().index, y=coluna.value_counts())
    ax.set_xlim(limites(coluna))
    plt.show()


# linhas que excluem os outliers
base_airbnb, linhas_removidas = excluir_outliers(base_airbnb, 'price')
# print(f"{linhas_removidas} linhas removidas na coluna de price")
#
# print(histograma(base_airbnb['price']))
# No primeiro gráfico não foi possível de analisar devido a grande quantidade de informações e por ser um gráfico nada intuitivo, mas nesse novo gráfico, podemos ver um comportamento humano de precificar um imóvel, podemos notar picos nos preços cheios (ex: 100, 200, 300..), pois é mais comum disso acontecer quando são possoas que precificam algo.

# Replicar o que a gente fez com a coluna de price para as outras sequências de colunas
# print(diagrama_caixa(base_airbnb['extra_people']))
# print(histograma(base_airbnb['extra_people']))

# linhas que excluem os outliers
base_airbnb, linhas_removidas = excluir_outliers(base_airbnb, 'extra_people')
# print(f"{linhas_removidas} linhas removidas na coluna de extra_people")
# print(histograma(base_airbnb['extra_people']))

# print("host_listing_count")
# print("host_listing_count")
# print("host_listing_count")

# host_listing_count
# print(diagrama_caixa(base_airbnb['host_listings_count']))
# print(grafico_barra(base_airbnb['host_listings_count']))

# Agora é só tirar os outliers para arrumar o eixo x
# Podemos excluir os outliers, porque para o objetivo do nosso projeto, hosts com mais de 6 imóveis no airbnb não é o alvo do objetivo do nosso projeto, entende-se que são imobiliárias ou profissionais que gerenciam vários imóveis no airbnb

base_airbnb, linhas_removidas = excluir_outliers(base_airbnb, 'host_listings_count')
# print(f"{linhas_removidas} linhas removidas na coluna de host_listings_count")
# print(histograma(base_airbnb['host_listings_count']))


### Accommodates
# print("Accommodates")
# print("Accommodates")
# print("Accommodates")


# print(diagrama_caixa(base_airbnb['accommodates']))
# print(grafico_barra(base_airbnb['accommodates']))

# Vamos excluir os imóveis que comportam mais do que 10 pessoas (que é o limite superior), porque são pouquíssimos imóveis e porque foge do nosso objetivo
# base_airbnb, linhas_removidas = excluir_outliers(base_airbnb, 'accommodates')
# print(f"{linhas_removidas} linhas removidas na coluna de accomodates")
# print(histograma(base_airbnb['accommodates']))

### bathrooms
# print("bathrooms")
# print("bathrooms")
# print("bathrooms")

# print(diagrama_caixa(base_airbnb['bathrooms']))
# print(grafico_barra(base_airbnb['bathrooms']))

# excluir outliers porque acima de 3,5 banheiros são pouquíssimos imóveis que tem
base_airbnb, linhas_removidas = excluir_outliers(base_airbnb, 'bathrooms')
# print(f"{linhas_removidas} linhas removidas na coluna de bathrooms")
# print(histograma(base_airbnb['bathrooms']))

## bedrooms
# print("bedrooms")
# print("bedrooms")
# print("bedrooms")
#
# print(diagrama_caixa(base_airbnb['bedrooms']))
# print(grafico_barra(base_airbnb['bedrooms']))
#
# # Poucos acima de 3 banheiros, a grande parte dos valores já estão dentro dos limites do gráfico
base_airbnb, linhas_removidas = excluir_outliers(base_airbnb, 'bedrooms')
# print(f"{linhas_removidas} linhas removidas na coluna de bedrooms")
# print(histograma(base_airbnb['bedrooms']))


## beds
# print("beds")
# print("beds")
# print("beds")
#
# print(diagrama_caixa(base_airbnb['beds']))
# print(grafico_barra(base_airbnb['beds']))
#
# # poucos imóveis que possuem acima de 6 camas
base_airbnb, linhas_removidas = excluir_outliers(base_airbnb, 'beds')
# print(f"{linhas_removidas} linhas removidas na coluna de beds")
# print(histograma(base_airbnb['beds']))


### Guests_included - quantas pessoas que quando você paga a diária já estão incluídas no pacote
# print("guests_included")
# print("guests_included")
# print("guests_included")
#
# print(diagrama_caixa(base_airbnb['guests_included']))
# print(grafico_barra(base_airbnb['guests_included']))

# no gráfico mostra que, tanto o nosso limite inferior quanto o nosso limite superior seriam considerados como 1.0
# vamos remover essa feature da análise, parece que os usuários do airbnb usam muito o padrão de valor do airbnb como um guest included, isso pode levar o nosso modelo a considerar uma feature que na verdade não é essencial para o valor do preço, por isso me parece melhor excluir a coluna da análise.

base_airbnb = base_airbnb.drop('guests_included', axis=1)

# base_airbnb, linhas_removidas = excluir_outliers(base_airbnb, 'guests_included')
# print(f"{linhas_removidas} linhas removidas na coluna de guests_included")
# print(histograma(base_airbnb['guests_included']))


### Minimum nights
# print("Minimum nights")
# print("Minimum nights")
# print("Minimum nights")
#
# print(diagrama_caixa(base_airbnb['minimum_nights']))
# print(grafico_barra(base_airbnb['minimum_nights']))
#
# # remover os outliers acima de 8 dias
base_airbnb, linhas_removidas = excluir_outliers(base_airbnb, 'minimum_nights')
# print(f"{linhas_removidas} linhas removidas na coluna de minimum_nights")
# print(histograma(base_airbnb['minimum_nights']))


### Maximum nights
# print("Maximum nights")
# print("Maximum nights")
# print("Maximum nights")
#
# print(diagrama_caixa(base_airbnb['maximum_nights']))
# print(grafico_barra(base_airbnb['maximum_nights']))

# Outro provável erro de preenchimento no airbnb pelos hosts, visto que a maioria dos valores são 0 e de que o nossos limites pegam valores muito altos, por isso vamos excluir a coluna

base_airbnb = base_airbnb.drop('maximum_nights', axis=1)


# number_of_reviews
# print("number_of_reviews")
# print("number_of_reviews")
# print("number_of_reviews")
#
# print(diagrama_caixa(base_airbnb['number_of_reviews']))
# print(grafico_barra(base_airbnb['number_of_reviews']))

# vamos excluir o número de reviews, porque o objetivo seria informar para uma pessoa o quanto ela poderia cobrar pelo imóvel dela, e sendo assim ela não teria review nenhum inicialmente.
base_airbnb = base_airbnb.drop('number_of_reviews', axis=1)

## Tratar features de texto

# prop type
# room type
# bad type
# amenities
# cancellation policy

# print(base_airbnb['property_type'].value_counts())

# plt.figure(figsize=(15, 5))
# grafico = sns.countplot("property_type", data=base_airbnb)
# grafico.tick_params(axis='x', rotation=90)
#
# plt.show()

# vou remover todos os tipos de imóveis que estão abaixo de 'others' pois estão em pequena quantidade e atribuir esses valores para 'others'


## Property type
tabela_tipos_imoveis = base_airbnb['property_type'].value_counts()
colunas_agrupar = []

for tipo in tabela_tipos_imoveis.index:
    if tabela_tipos_imoveis[tipo] <= 6000:
        # retorna a quantidade de cada tipo de imóvel
        # originalmente temos 5845 em others, então todos que forem menor do que isso...
        colunas_agrupar.append(tipo)
        # Uma lista com todas as colunas que eu vou considerar como outros

for tipo in colunas_agrupar:
    base_airbnb.loc[base_airbnb['property_type'] == tipo, 'property_type'] = "Outros"
    # vou localizar na minha tabela todas as linhas que são igual ao tipo
#
# print(base_airbnb['property_type'].value_counts())


# Room Type
# Por temos somente 4 categorias não vai fazer diferença na nossa análise e por isso não precisamos tratar essa coluna


# bed_type
# Podemos ver que essa coluna tinha somente 4 categorias de camas, onde quase 100% eram do tipo "Real bed" e as outras tinham valores insignificantes. No video o Lira optou por deixar, assim como fizemos na coluna de 'room_type', mas disse também que seria uma boa agrupar as outras opções visto que o valor da 'Real bed' era muito alto e de que o nosso modelo também se sairia bem analisando esse fator, pois ele enxergaria basicamente como 'sim ou não', visto que agora só temos 'Real bed' e 'Outras Camas'
# print(base_airbnb['bed_type'].value_counts())
#
tabela_tipos_cama = base_airbnb['bed_type'].value_counts()
colunas_agrupar = []


for tipo in tabela_tipos_cama.index:
    if tipo != "Real Bed":
        colunas_agrupar.append(tipo)

for tipo in colunas_agrupar:
    base_airbnb.loc[base_airbnb['bed_type'] == tipo, 'bed_type'] = "Outras camas"
# vou achar as linhas que são igual ao tipo e substituir o valor por 'Outras camas'


# print(base_airbnb['bed_type'].value_counts())


### Cancellation policy
# Temos predominantemente 3 categorias e outras 3 categorias com valores muito baixos, na qual iremos agrupar como uma opção só
# print(base_airbnb['cancellation_policy'].value_counts())
#
# plt.figure(figsize=(15, 5))
# grafico = sns.countplot("cancellation_policy", data=base_airbnb)
# grafico.tick_params(axis='x', rotation=90)
#
# plt.show()
#
tabela_tipos_cancelamento = base_airbnb['cancellation_policy'].value_counts()
colunas_agrupar = []


for tipo in tabela_tipos_cancelamento.index:
    if tabela_tipos_cancelamento[tipo] <= 260000:
        colunas_agrupar.append(tipo)

for tipo in colunas_agrupar:
    base_airbnb.loc[base_airbnb['cancellation_policy'] == tipo, 'cancellation_policy'] = "strict"
#
# # diferença entre os gráficos
# plt.figure(figsize=(15, 5))
# grafico = sns.countplot("cancellation_policy", data=base_airbnb)
# grafico.tick_params(axis='x', rotation=90)
#
# plt.show()
# print(base_airbnb['cancellation_policy'].value_counts())


# Amenities
# Ao invés de analisar os itens dentro de amenities (que são bagunçados, escritos de muitas formas diferentes, e informações que as vezes são desnecessárias), eu vou analisar o tamanho do objeto amenities, com a lógica de que, quanto maior aquele objeto, o imóvel pode sim ter mais coisas/comodidades que outros, mas significa também que o host pelo menos se esforçou mais no anúncio daquele imóvel e de que isso pode impactar no valor final.

base_airbnb['n_amenities'] = base_airbnb['amenities'].str.split(",").apply(len)
# Vai me dar a quantidade de amenities que tem naquelas linhas

base_airbnb = base_airbnb.drop("amenities", axis=1)

# Agora que pegamos o len da coluna de amenities, ela virou uma coluna numérica, então nós podemos tratar ela igual tratamos outras colunas e também excluir os outliers

# print(diagrama_caixa(base_airbnb['n_amenities']))
# print(grafico_barra(base_airbnb['n_amenities']))

base_airbnb, linhas_removidas = excluir_outliers(base_airbnb, 'n_amenities')
# print(f"{linhas_removidas} linhas removidas na coluna de n_amenities")
# print(histograma(base_airbnb['n_amenities']))


# Vizualização de mapa das propriedades, latitude e longitude
# Definir o tamanho
amostra = base_airbnb.sample(n=50000) # vai pegar 50 mil valores aleatórios, pra tornar mais rápido, leve
# Definir onde vai ser o mapa
centro_mapa = {"lat": amostra.latitude.mean(), "lon": amostra.longitude.mean()}
# z = mudar de cor de acordo com o preço
# radius = o raio de cada bolinha que representa o texto
# center = é o centro da média que fizemos no dicionário acima, de latitude e longitude
mapa = px.density_mapbox(amostra, lat="latitude", lon="longitude", z="price", radius=2.5, center=centro_mapa, zoom=10, mapbox_style="stamen-terrain")

mapa.show()

# Encoding
# Precisamos ajustar as features para facilitar o trabalho do modelo futuro (features de categoria, true e false, etc.)
# True or False = T:1 F:0
# para features de categoria vamos utilizar o método de encoding de variáveis dummies

colunas_tf = ["host_is_superhost", "instant_bookable", "is_business_travel_ready"]
colunas_categorias = ["property_type", "room_type", "bed_type", "cancellation_policy"]

# Codificação das colunas t/f
base_airbnb_cod = base_airbnb.copy()
for column in base_airbnb:
    base_airbnb_cod.loc[base_airbnb_cod[column] == "t", column] = 1
    base_airbnb_cod.loc[base_airbnb_cod[column] == "f", column] = 0


# Codificação das colunas de categorias (usando dummies)
base_airbnb_cod = pd.get_dummies(data=base_airbnb_cod, columns=colunas_categorias)
# pd.get_dummies te dá como resposta um DataFrame que vai transformar algumas colunas em dummies


# Tudo que fizemos até agora foi preparar a nossa base de dados para aplicar nossos modelos nela


### Modelo de previsão
# Usando a biblioteca Sklearn - Biblioteca de inteligência artificial
# R² e o Erro quadrático médio

def avaliar_modelo(nome_modelo, y_teste, previsao):
    """
    :param nome_modelo: Só para poder printar o nome do nosso modelo
    :param y_teste: Valores reais/Corretos que vão ser usados para testar nosso modelo
    :param previsao: Vamos ver se a previsão está perto ou não do valor correto e depois julgar se o modelo é bom ou ruim
    :return:
    """

    # Métricas de avaliação
    r2 = r2_score(y_teste, previsao)
    RSME = np.sqrt(mean_squared_error(y_teste, previsao))
    # Vai tirar a raiz quadrada do mean squared error
    return f"Modelo: {nome_modelo}\nR²: {r2}\nRSME: {RSME}"

    # Pegando as previsões e comparando com os testes seguindo duas métricas


# Escolha dos modelos a serem testados
# Esses modelos já foram criados para gente (todos na mesma biblioteca do sklearn), só precisamos entender como funciona e como se aplica, e não conhecer os mínimos detalhes de cada um (pelo menos inicialmente).
# 1 - Random Forest
# 2 - Linear Regression
# 3 - Extra trees

modelo_rf = RandomForestRegressor()
modelo_lr = LinearRegression()
modelo_et = ExtraTreesRegressor()

modelos = {
    "RandomForest": modelo_rf,
    "LinearRegression": modelo_lr,
    "ExtraTrees": modelo_et
}

# Separação das variáveis
y = base_airbnb_cod['price']
x = base_airbnb_cod.drop('price', axis=1)

# Separar os dados em treino e teste + Treino do modelo
# Tenho que fazer essa separação tanto para as colunas quanto para o preço que é o que eu quero calcular

# ""Olha as característica desses 8 imóveis aqui, agora, com base nesses dados que você viu, precifica para mim esses novos dois imóveis com base no seu conhecimento""

# E também já temos um modelo pronto de separação dentro do sklearn
# train_test_split = Vai fazer um split em dados de treino e em dados de teste

x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=10)
# Random_state _ estou determinando ele à usar sempre como semente o número 10, a vantagem é de que se eu rodar os códigos outras vezes, ele vai fazer a mesma divisão na base de dados, e não vai ficar mudando os dados de teste / treino

# Agora precisamos treinar e testar cada um dos modelos
for nome_modelo, modelo in modelos.items():
    # Treinar
    modelo.fit(x_train, y_train)
    # Testar
    previsao = modelo.predict(x_test)
    print(avaliar_modelo(nome_modelo, y_test, previsao))


# Modelo: RandomForest
# R²: 0.9855938815939891 - 98.56%
# RSME: 31.79745982390543
#
# Modelo: LinearRegression
# R²: 0.3268426558013201 - 32.68%
# RSME: 217.35880184606643
#
# Modelo: ExtraTrees
# R²: 0.9874667994490411 - 98.75%
# RSME: 29.658551173359623

# - Melhor modelo: # Modelo: ExtraTrees
# Esse foi o modelo com maior valor de R² e ao mesmo tempo o menor valor de RSME
# Não tivemos grande diferença de velocidade entre ele e o segundo colocado
# O modelo de regressão linear não teve um resultado satisfatório, muito pior do que os outros modelos


# Agora que a gente já escolheu o nosso melhor modelo, agora vamos entender como ele tá funcionando e ver possíveis melhorias

# Nossos modelos tem uma função que exibe a importância de cada feature, que ele levou em consideração na sua análise. Assim podemos ver as colunas mais importantes e também as colunas que ele não utiliza ou que quase não leva em consideração, e assim nós podemos remover elas e melhorar ainda mais o nosso modelo.

importancia_features = pd.DataFrame(modelo_et.feature_importances_, x_train.columns)
importancia_features.sort_values(by=0, ascending=True, inplace=True)

plt.figure(figsize=(15, 5))
ax = sns.barplot(x=importancia_features.index, y=importancia_features[0])
ax.tick_params(axis="x", rotation=90)


# Latitude e longitude de fato é realmente muito importante e já era de se imaginar que ía ficar em primeiro. devido a localização que é próximo as praias, próximo aos pontos turísticos, locais mais seguros, faz sentido o imóvel ser mais caro

# quantidade de quartos

# amenities surpreendendo. Pode ser que ,no caso dos amenities que detalharam mais as casas realmente tenham mais coisas ou que os amenities que tem menos é porque o host não entra tanto a fundo no anúncio e não consegue cobrar um preço mais alto pelo seu imóvel

# Detalhar mais um pouco sobre as outras colunas....

# Ajustes finais
# A colunas is_business_travel_ready não tem nenhum grau de importância no resultado da função de importância de features, por isso vamos tirar ela da nossa base de dados e treinar o nosso modelo novamente para ver se as nossas métricas melhoram ou não

base_airbnb_cod = base_airbnb_cod.drop("is_business_travel_ready", axis=1)

y = base_airbnb_cod['price']
x = base_airbnb_cod.drop('price', axis=1)

# Tirando as colunas de cama (mais para teste mesmo e porque ela tiveram uma importância baixa)

base_teste = base_airbnb_cod.copy()
for coluna in base_teste:
    if "bed_type" in coluna:
        base_teste = base_teste.drop(coluna, axis=1)

y = base_teste['price']
x = base_teste.drop("price", axis=1)

x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=10)

modelo_et.fit(x_train, y_train)
previsao = modelo_et.predict(x_test)
print(avaliar_modelo('ExtraTrees', y_test, previsao))


### Deploy do projeto
# 1 - Criar um arquivo do nosso modelo já treinado usando i picle da biblioteca joblib
# 2 - Escolher a forma de deploy:
#     - Arquivo exe + Tkinter
#     - Deploy em um microsite (Flask)
#     - Deploy para uso direto (Streamlit)



x['price'] = y
x.to_cvs("dados.csv")

import joblib
joblib.dump(modelo_et, "modelo.joblib") # é um arquivo pesado mas dentro dele já está o modelo pronto