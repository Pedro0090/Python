# PROGRAMA QUE MOSTRA O FATORIAL DE UM NÚMERO (3 JEITOS DIFERENTES)
"""from math import factorial

n = int(input('Digite um número para calcular seu fatorial: '))
f = factorial(n)
print(f'O fatorial de {n} é {f}.')"""
n = int(input('Digite um número para calcular seu fatorial: '))
c = n
print(f'{n}! = ', end='')
f = 1
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f)
'''n = int(input('Digite um número para calcular seu fatorial: '))
f = 1
print(f'{n}! = ', end='')
for c in range (n, 0, -1):
    print(c, end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
print(f'{f}')'''
