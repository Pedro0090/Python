# USO DE FUÇÕES QUE SORTEIAM E SOMAM OS PARES DE UMA LISTA
from random import randint


def sorteio(lst):
    print('Sorteando 5 valores da lista: ', end='')
    for i in range(0, 5):
        n = randint(0, 10)
        lst.append(n)
        print(n, end=' ')
    print('PRONTO!')


def somapar(lst):
    t = 0
    for v in lst:
        if v % 2 == 0:
            t += v
    print(f'Somando os valores pares de {lst} temos {t}')


val = []
sorteio(val)
somapar(val)
