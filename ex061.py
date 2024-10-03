# PROGRESSÃO ARITMÉTICA COM WHILE
print('GERADOR DE PA')
print('-=' * 10)
n = int(input('Primeiro termo = '))
r = int(input('Razão: '))
termo = n
c = 1
while c <= 10:
    print(f'{termo} → ', end='')
    termo += r
    c += 1
print('FIM')
