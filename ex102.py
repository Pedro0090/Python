def fatorial(x, show=False):
    """
    -> Calcula o fatorial de um número
    :param x: Número que deseja para ser calculado o fatorial
    :param show: Opcional. Se for igual a "True" mostrará a conta toda, caso contrário mostrará apenas o resultado
    :return: Retorna o resultado do fatorial do valor
    """
    f = 1
    for n in range(x, 0, -1):
        if show:
            print(n, end='')
            print(' x ' if n != 1 else ' = ', end='')
        f *= n
    return f


print('-' * 30)
print(fatorial(6, True))
