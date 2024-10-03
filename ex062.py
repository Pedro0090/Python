# SUPER PROGRESSÃO ARITMÉTICA
print('GERADOR DE PA')
print('-=' * 10)
n = int(input('Primeiro termo = '))
r = int(input('Razão: '))
termo = n
c = 1
sequenc = 10
total = 0
while sequenc != 0:
    total += sequenc
    while c <= total:
        print(f'{termo} → ', end='')
        termo += r
        c += 1
    print('PAUSA')
    sequenc = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Programa finalizado com {total} termos')
