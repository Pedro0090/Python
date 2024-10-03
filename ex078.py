# PROGRAMA QUE LÊ 5 NÚMEROS, MOSTRA O MAIOR VALOR, O MENOR VALOR, E, SUAS RESPECTIVAS POSIÇÕES
valores = []
for c in range(0, 5):
    valores.append(int(input(f'Digite o valor para a posição {c}: ')))
print('-=' * 30)
maior = max(valores)
menor = min(valores)
print(f'você digitou os valores: {valores}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for pos, v in enumerate(valores):
    if v == maior:
        print(f'{pos}... ', end='')
print(f'\nO menor valor digitado foi {menor} nas posições ', end='')
for pos, v in enumerate(valores):
    if v == menor:
        print(f'{pos}... ', end='')
