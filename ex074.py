# PROGAMA QUE SORTEIA NÚMEROS E DIZ QUAL O MAIOR E MENOR VALOR
from random import randint


ns = randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)
print(f'Os valores sorteados foram ', end='')
for n in ns:
    print(n, end=' ')
print(f'\nO maior valor sorteado foi {max(ns)}')
print(f'O menor valor sorteado foi {min(ns)}')
