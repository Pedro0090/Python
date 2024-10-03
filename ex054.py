# PROGRAMA PEDE DATAS DE NASCIMENTO DE 7 PESSOAS E IDENTIFICA QUANTOS SÃO MAIORES E QUANTOS SÃO MENORES DE IDADE (21)
from datetime import date

maior = 0
menor = 0
for p in range(1, 8):
    ano = int(input(f'Em que ano a {p}ª pessoa nasceu? '))
    idade = date.today().year - ano
    if idade < 21:
        menor += 1
    else:
        maior += 1
print(f'Ao todo tivemos {maior} pessoas maiores de idade')
print(f'E também tivemos {menor} pessoas menores de idade')
