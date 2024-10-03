# PROGRAMA QUE MOSTRA INFORMAÇÕES DE UMA PESSOA COM CARTEIRA DE TRABALHO (OU SEM)
from datetime import datetime

tb = {}
tb['nome'] = str(input('Nome: ')).strip()
ano = int(input('Ano de nascimento: '))
tb['idade'] = datetime.now().year - ano
tb['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if tb['ctps'] > 0:
    anocont = int(input('Ano de contratação: '))
    tb['contratação'] = datetime.now().year - anocont
    tb['salário'] = float(input('Salário: R$'))
    tb['aposentadoria'] = tb['idade'] + ((tb['contratação'] + 35) - datetime.now().year)
print('-=' * 30)
for k, v in tb.items():
    print(f'  - {k} é {v}')
