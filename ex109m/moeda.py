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
