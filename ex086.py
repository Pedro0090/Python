# PROGRAMA QUE PEDE 9 NÚMEROS E OS ORGANIZA EM UMA MATRIZ
tabela = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        tabela[l][c] = int(input(f'Digite o valor para [{l}, {c}]: '))
print('-=' *30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{tabela[l][c]:^5}]', end='')
    print()
