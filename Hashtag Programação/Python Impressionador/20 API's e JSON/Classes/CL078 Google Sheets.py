# Mentolira

from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# If modifying these scopes, delete the file token.json.
# modificar tirando o .readonly do final
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID and range of a sample spreadsheet.
# escolher a planilha que quer conectar e um range só para conferir se conectou
SAMPLE_SPREADSHEET_ID = "1uaj6AfosjGjOYhIJpOiIl6kEhQ1DEb34"
SAMPLE_RANGE_NAME = 'Página1!A1:A5'


"""Shows basic usage of the Sheets API.
Prints values from a sample spreadsheet.
"""
creds = None
# The file token.json stores the user's access and refresh tokens, and is
# created automatically when the authorization flow completes for the first
# time.
if os.path.exists('token.json'):
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
# If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials_2.json', SCOPES)
        creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open('token.json', 'w') as token:
        token.write(creds.to_json())

service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range=SAMPLE_RANGE_NAME).execute()
values = result.get('values', [])

if not values:
    print('No data found.')
else:
    print("Conexão Bem sucedida")

# a partir daqui a gente vai brincar com os comandos do Google Sheets


# pegar valores de um conjunto de células
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="Página2!A1:C3").execute()
values = result.get('values', [])
print(values)

# escrever valores no google sheets
values = [
    [
        "Faturamento: R$2.500"
    ],
]
body = {
    'values': values
}
result = service.spreadsheets().values().update(
    spreadsheetId="1cwxg-Z6NWAKHvwAQwdrU8YPpPVG68ACyalhw1WCf5ZE",
    range="Página3!A1",
    valueInputOption="USER_ENTERED", body=body).execute()

# adicionar um valor no final da tabela
# values = [
#     [
#         "Lira", "lira@gmail.com", "Sem Dinheiro"
#     ],
# ]
# body = {
#     'values': values
# }
# result = service.spreadsheets().values().append(
#     spreadsheetId="11PhF4YyWQgnYSweZ6TEGdX8n48EaRRlw_0h3cgo2ESo",
#     range="Página1!A1",
#     valueInputOption="USER_ENTERED", body=body).execute()

# mini-desafio -> Recuperação de Vendas da Hashtag

# Passo 1: Ler o intervalo de células
result = sheet.values().get(spreadsheetId="11PhF4YyWQgnYSweZ6TEGdX8n48EaRRlw_0h3cgo2ESo",
                            range="Página1!A2:D9").execute()
values = result.get('values', [])
print(values)
# Passo 2: Verificar se o status está preenchido
linha = 2
for lista in values:
    # Passo 3: Se o status não tá preenchido, verificar o Problema
    if len(lista) < 4:
        if lista[2] == "Boleto Gerado":
            print("Enviar Mensagem do Boleto")
            # preencher a coluna Status com "Mensagem do Boleto enviada"

            values = [
                [
                    "Mensagem do Boleto enviada"
                ],
            ]
            body = {
                'values': values
            }
            result = service.spreadsheets().values().update(
                spreadsheetId="11PhF4YyWQgnYSweZ6TEGdX8n48EaRRlw_0h3cgo2ESo",
                range=f"Página1!D{linha}",
                valueInputOption="USER_ENTERED", body=body).execute()


        elif lista[2] == "Comprou":

            values = [
                [
                    "Compra Finalizada"
                ],
            ]
            body = {
                'values': values
            }
            result = service.spreadsheets().values().update(
                spreadsheetId="11PhF4YyWQgnYSweZ6TEGdX8n48EaRRlw_0h3cgo2ESo",
                range=f"Página1!D{linha}",
                valueInputOption="USER_ENTERED", body=body).execute()

        elif lista[2] == "Sem Saldo":
            print("Enviar Mensagem Sem Saldo no Cartão")
            # preencher a coluna Status com "Mensagem do Boleto enviada"

            values = [
                [
                    "Mensagem Sem Saldo enviada"
                ],
            ]
            body = {
                'values': values
            }
            result = service.spreadsheets().values().update(
                spreadsheetId="11PhF4YyWQgnYSweZ6TEGdX8n48EaRRlw_0h3cgo2ESo",
                range=f"Página1!D{linha}",
                valueInputOption="USER_ENTERED", body=body).execute()

    linha += 1
# Passo 4: Enviar Mensagem e registrar novo status