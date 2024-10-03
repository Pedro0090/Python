# PROGRAMA QUE REALIZA CONTAGENS ATRAVÉS DE FUNÇÕES
from time import sleep


def contador(i, f, p):
    print('-=' * 30)
    print(f'Contagem de {i} a {f} de', end=' ')
    print(f'{p} em {p}' if p > 0 else f'{p * (-1)} em {p * (-1)}')
    sleep(1.5)
    if p == 0:
        p = -1
    if p < 0:
        f -= 2
    if i < 0 and p < 0:
        p *= -1
    for c in range(i, f + 1, p):
        print(c, end=' ')
        sleep(0.5)
    print('FIM!')


contador(1, 10, 1)
contador(10, 0, -2)
print('-=' * 30)
print('Agora é a sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim:     '))
passo = int(input('Passo:  '))
contador(inicio, fim, passo)
