import re
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
from termcolor import colored

# Pega o conteúdo da página
page = requests.get('https://ri.br.com.br/informacoes-financeiras/dividendos-e-jcp/')
soup = BeautifulSoup(page.content, 'html.parser')

# Seleciona os dados de cabeçalho e das linhas da tabela
header = soup.select('#wp-content table thead tr')
rows = soup.select('#wp-content table tbody tr')

# Separa os textos de cada coluna do cabeçalho em um array
headerData = []
for head in header[0].select('th'):
    headerData.append(head.get_text().replace('\n', ' '))

# Separa os textos de cada coluna do corpo da tabela em outro array
rowsData = []
sumIndex = 4
total = 0
for row in rows:
    rowData = []
    shouldSum = False

    for i, col in enumerate(row.select('td')):
        val = col.get_text()
        cleaned = re.sub(r'R\$\s*', '', val)
        if re.match(r'[0-9]{2}\/[0-9]{2}\/[0-9]{4}', cleaned):
            color = 'red'
            if re.match(r'[0-9]{2}\/[0-9]{2}\/[0-9]{2}19', cleaned):
                shouldSum = True
                color = 'green'
            cleaned = colored(cleaned, color)
        rowData.append(cleaned)

        if i == sumIndex and shouldSum:
            total += float(cleaned.replace(',','.'))

    rowsData.append(rowData)


print(tabulate(rowsData, headers=headerData))

print()
print('Total de 2019')
print(total)

