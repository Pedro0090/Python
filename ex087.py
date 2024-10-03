# PROGRAMA MATRIZ COM ALGUNS DADOS ADICIONAIS
tabela = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = c3 = 0
for l in range(0, 3):
    for c in range(0, 3):
        tabela[l][c] = int(input(f'Digite o valor para [{l}, {c}]: '))
        if tabela[l][c] % 2 == 0:
            par += tabela[l][c]
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{tabela[l][c]:^5}]', end='')
    print()
print('-=' * 30)
print(f'A soma dos pares é {par}')
# c3 = tabela[0][2] + tabela[1][2] + tabela[2][2]
for l in range(0, 3):
    c3 += tabela[l][2]
print(f'A soma dos valores da terceira coluna é {c3}')
print(f'O maior valor da segunda linha é {max(tabela[1])}')
