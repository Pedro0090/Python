# ROGRAMA QUE PEGA O PESO DE ALGUMAS PESSOAS E DIZ POR MEIO DE LISTAS O NOME DOS MAIS PESADOS, MAIS LEVE, QUANTIDADE DE
# PESSOAS CADASTRADAS E MAIS
np = []
dados = []
pesos = []
while True:
    np.append(str(input('Nome: ').strip()))
    np.append(float(input('Peso: ')))
    dados.append(np[:])
    np.clear()
    cont = ' '
    while cont not in 'SsNn':
        cont = str(input('Quer continuar? [S/N] ')).strip()
    if cont in 'Nn':
        break
for p in dados:
    pesos.append(p[1])
mai = max(pesos)
men = min(pesos)
print('-=' * 30)
print(f'Foram cadastradas {len(dados)} pessoas.')
print(f'O maior peso foi de {mai}Kg. Peso de ', end='')
for p in dados:
    if p[1] == mai:
        print(f'[{p[0]}]', end=' ')
print(f'\nO menor peso foi de {men}Kg. Peso de ', end='')
for p in dados:
    if p[1] == men:
        print(f'[{p[0]}]', end=' ')
