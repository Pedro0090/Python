# PROGRAMA QUE MOSTRA SE O NÚMERO É PRIMO
tot = 0
n1 = int(input('Digite um número: '))
for i in range(1, n1+1):
    if n1 % i == 0:
        print('\033[31m' , end=' ')
        tot += 1
    else:
        print('\033[33m', end= ' ')
    print(f'{i}', end= ' ')
print(f'\n\033[mO número {n1} foi divisível {tot} vezes.')
if tot == 2:
    print('Por isso ele É PRIMO.')
else:
    print('Por isso ele NÃO É PRIMO.')
