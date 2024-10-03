def anos(x):
    from datetime import date
    idade = date.today().year - x
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 70 > idade >= 18:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'
    else:
        return f'Com {idade} anos: VOTO OPCIONAL.'


print('-' * 30)
ano = int(input(f'Em que ano você nasceu? '))
print(anos(ano))
