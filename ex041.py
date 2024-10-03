# PROGRAMA QUE LÊ A IDADE DE UM ATLETA A PARTIR DO ANO DE NASCIMENTO E DIZ QUAL CATEGORIA ELE SE ENCAIXA
from datetime import date

ano = int(input('Digite o ano de nascimento do atleta: '))
categoria = (date.today().year) - ano
if categoria <= 9:
    print(f'O atleta tem {categoria} anos.')
    print('Categoria: MIRIM!')
elif categoria <= 14:
    print(f'O atleta tem {categoria} anos.')
    print('Categoria: INFANTIL!')
elif categoria <= 19:
    print(f'O atleta tem {categoria} anos.')
    print('Categoria: JUNIOR!')
elif categoria <= 25:
    print(f'O atleta tem {categoria} anos.')
    print('Categoria: SÊNIOR!')
else: 
    print(f'O atleta tem {categoria} anos.')
    print('Categoria: MASTER!')
