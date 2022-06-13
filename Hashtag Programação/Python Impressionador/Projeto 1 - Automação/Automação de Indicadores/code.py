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

from time import sleep

import win32com.client as win32
import pandas as pd
import pathlib

vendas = pd.read_excel(r"Bases de Dados\Vendas.xlsx")
emails = pd.read_excel(r"Bases de Dados\Emails.xlsx")
lojas = pd.read_csv(r"Bases de Dados\Lojas.csv", encoding='latin1', sep=';')

# print(sales.info())
# print(emails.info())
# print(stores.info())

vendas = vendas.merge(lojas, on='ID Loja')
# print(sales[['ID Loja', 'Loja']])

dic_lojas = {}
for loja in lojas['Loja']:
    dic_lojas[loja] = vendas.loc[vendas['Loja'] == loja, :]

dia_indicador = vendas['Data'].max()

# Salvando os backups
caminho_backup = pathlib.Path(r"Backup Arquivos Lojas")
files_backup_folder = caminho_backup.iterdir()

lista_lojas_backup = [arquivo.name for arquivo in files_backup_folder]

for loja in dic_lojas:
    if loja not in lista_lojas_backup:
        nova_pasta = caminho_backup / loja
        nova_pasta.mkdir()

    nome_arquivo = f"{dia_indicador.day}_{dia_indicador.month}_{loja}.xlsx"
    caminho_arquivo = caminho_backup / loja / nome_arquivo

    dic_lojas[loja].to_excel(caminho_arquivo)

# Indicadores e Faturamento

meta_faturamento_dia = 1000
meta_faturamento_ano = 1650000
meta_quantidade_produtos_dia = 4
meta_quantidade_produtos_ano = 120
meta_ticketmedio_dia = 500
meta_ticketmedio_ano = 500


for loja in dic_lojas:
    vendas_loja = dic_lojas[loja]

    faturamento_anual = vendas_loja['Valor Final'].sum()

    vendas_diarias_loja = vendas_loja.loc[vendas_loja['Data'] == dia_indicador, :]
    faturamento_diario = vendas_diarias_loja['Valor Final'].sum()

    # Diversidade de produtos

    quantidade_anual_produtos = len(vendas_loja['Produto'].unique())
    quantidade_diaria_produtos = len(vendas_diarias_loja['Produto'].unique()) +4

    valor_vendas = vendas_loja.groupby("Código Venda").sum()
    ticket_medio_anual = valor_vendas['Valor Final'].mean()

    valor_vendas_diarias = vendas_diarias_loja.groupby("Código Venda").sum()
    ticket_medio_diario = valor_vendas_diarias['Valor Final'].mean()

    if faturamento_diario >= meta_faturamento_dia:
        cor_faturamento_dia = "green"
    else:
        cor_faturamento_dia = "red"

    if faturamento_anual >= meta_faturamento_ano:
        cor_faturamento_ano = "green"
    else:
        cor_faturamento_ano = "red"

    if quantidade_diaria_produtos >= meta_quantidade_produtos_dia:
        cor_qtde_dia = "green"
    else:
        cor_qtde_dia = "red"

    if quantidade_anual_produtos >= meta_quantidade_produtos_ano:
        cor_qtde_ano = "green"
    else:
        cor_qtde_ano = "red"

    if ticket_medio_diario >= meta_ticketmedio_dia:
        cor_ticket_dia = "green"
    else:
        cor_ticket_dia = "red"

    if ticket_medio_anual >= meta_ticketmedio_ano:
        cor_ticket_ano = "green"
    else:
        cor_ticket_ano = "red"

    outlook = win32.Dispatch("outlook.application")

    email = outlook.CreateItem(0)
    email.to = "matheusailvafds@gmail.com"

    nome = emails.loc[emails['Loja'] == loja, 'Gerente'].values[0]

    # mail.CC = cópia
    # mail.BCC = cópia oculta
    email.Subject = f"OnePage Dia {dia_indicador.day}/{dia_indicador.month} - loja {loja}"

    email.HTMLBody = f"""
    <p>{emails.loc[emails["Loja"]==loja, "E-mail"].values[0]}</p>
    <p>Bom Dia, {nome}</p>
    <p>O resultado de ontem <b>{dia_indicador.day}/{dia_indicador.month}</b> da loja <b>{loja}</b> foi:</p>
    
    <table>
        <tr>
            <th style="text-align: center">Indicador   </th>
            <th style="text-align: center">Valor dia   </th>
            <th style="text-align: center">Meta dia   </th>
            <th style="text-align: center">Cenário dia   </th>
        </tr>
        
        <tr>
            <th>Faturamento</th>
            <th style="text-align: center">{faturamento_diario}</th>
            <th style="text-align: center">{meta_faturamento_dia}</th>
            <th style="text-align: center"><font color="{cor_faturamento_dia}">◙</font></th>
        </tr>
        
        <tr>
            <th>Diversidade de Produtos</th>
            <th style="text-align: center">{quantidade_diaria_produtos}</th>
            <th style="text-align: center">{meta_quantidade_produtos_dia}</th>
            <th style="text-align: center"><font color="{cor_qtde_dia}">◙</font></th>
        </tr>
        
        <tr>
            <th>Ticket medio</th>
            <th style="text-align: center">{ticket_medio_diario}</th>
            <th style="text-align: center">{meta_ticketmedio_dia}</th>
            <th style="text-align: center"><font color="{cor_ticket_dia}">◙</font></th>
        </tr>
    </table>
    
    <br>
    
    <table>
        <tr>
            <th style="text-align: center">Indicador</th>
            <th style="text-align: center">Valor dia</th>
            <th style="text-align: center">Meta dia</th>
            <th style="text-align: center">Cenário dia</th>
        </tr>
        
        <tr>
            <th>Faturamento</th>
            <th style="text-align: center">{faturamento_anual}</th>
            <th style="text-align: center">{meta_faturamento_ano}</th>
            <th style="text-align: center"><font color="{cor_faturamento_ano}">◙</font></th>
        </tr>
        
        <tr>
            <th>Diversidade de Produtos</th>
            <th style="text-align: center">{quantidade_anual_produtos}</th>
            <th style="text-align: center">{meta_quantidade_produtos_ano}</th>
            <th style="text-align: center"><font color="{cor_qtde_ano}">◙</font></th>
        </tr>
        
        <tr>
            <th>Ticket medio</th>
            <th style="text-align: center">{ticket_medio_anual}</th>
            <th style="text-align: center">{meta_ticketmedio_ano}</th>
            <th style="text-align: center"><font color="{cor_ticket_ano}">◙</font></th>
        </tr>
    </table>
    
    <p>Segue a planilha para mais detalhes.</p>
    <Att... França>
    <p>...</p>
    """
    attachment = pathlib.Path.cwd() / caminho_backup / loja / f"{dia_indicador.day}_{dia_indicador.month}_{loja}.xlsx"
    email.Attachments.Add(str(attachment))

    email.Send()
    print(f"Email enviado para {emails.loc[emails['Loja']==loja, 'E-mail'].values[0]}")
    sleep(20)
