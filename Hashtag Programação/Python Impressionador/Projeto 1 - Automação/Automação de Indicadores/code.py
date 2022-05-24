"""
Com base em 3 planilhas você precisará enviar um E-mail toda manhã para um determiado gerente com indicador 1, 2 e 3
por dia e por ano e que a diretoria receba um ranking das lojas por dia e por ano, e que salve esses arquivos em pastas
separadas como forma de backup.


Automação de Indicadores
Objetivo: Treinar e criar um Projeto Completo que envolva a automatização de um processo feito no computador
Descrição:
Imagine que você trabalha em uma grande rede de lojas de roupa com 25 lojas espalhadas por todo o Brasil.

Todo dia, pela manhã, a equipe de análise de dados calcula os chamados One Pages e envia para o gerente de cada loja o
 OnePage da sua loja, bem como todas as informações usadas no cálculo dos indicadores.

Um One Page é um resumo muito simples e direto ao ponto, usado pela equipe de gerência de loja para saber os principais
indicadores de cada loja e permitir em 1 página (daí o nome OnePage) tanto a comparação entre diferentes lojas, quanto
quais indicadores aquela loja conseguiu cumprir naquele dia ou não.
"""

# 1 - Importar e tratar as bases de dados
# 2 - Criar 1 arquivo para cada loja
# 3 - Salvar o arquivo nas pastas
# 4 - Calcular os indicadores
# 5 - Enviar o OnePage
# 6 - Enviar o E-mail para a diretoria

import pandas as pd
import pathlib

sales = pd.read_excel(r"Bases de Dados\Vendas.xlsx")
emails = pd.read_excel(r"Bases de Dados\Emails.xlsx")
stores = pd.read_csv(r"Bases de Dados\Lojas.csv", encoding='latin1', sep=';')

# print(sales.info())
# print(emails.info())
# print(stores.info())

sales = sales.merge(stores, on='ID Loja')
# print(sales[['ID Loja', 'Loja']])

dic_stores = {}
for store in stores['Loja']:
    dic_stores[store] = sales.loc[sales['Loja'] == store, :]

dia_indicador = sales['Data'].max()
# Salvando os Backups
backup_path = pathlib.Path(r"Backup Arquivos Lojas")
files_backup_folder = backup_path.iterdir()

list_stores_backup = [file.name for file in files_backup_folder]

print(list_stores_backup)

for store in dic_stores:
    if store not in list_stores_backup:
        new_folder = backup_path / store
        new_folder.mkdir()

    file_name = f"{dia_indicador.day}_{dia_indicador.month}_{store}.xlsx"
    print(file_name)
    file_path = backup_path / store / file_name

    dic_stores[store].to_excel(file_path)