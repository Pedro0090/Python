def metade(x=0, fmt=False):
    res = x / 2
    return res if not fmt else moeda(res)


def dobro(x=0, fmt=False):
    res = x * 2
    return res if not fmt else moeda(res)


def aumentar(x=0, t=0, fmt=False):
    res = x + (x * t / 100)
    return res if not fmt else moeda(res)


def diminuir(x=0, t=0, fmt=False):
    res = x - (x * t / 100)
    return res if not fmt else moeda(res)


def moeda(x=0.0, m='R$'):
    return f'{m}{x:.2f}'.replace('.', ',')


def resumo(x=0, a=10, d=5):
    print('-' * 30)
    print(f'RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço Análisado: \t{moeda(x)}')
    print(f'Dobro do preço: \t{dobro(x, True)}')
    print(f'{a}% de aumento: \t{aumentar(x, a, True)}')
    print(f'{d}% de redução: \t{diminuir(x, d, True)}')
    print('-' * 30)
