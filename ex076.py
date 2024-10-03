# MOSTRA UMA TABELA FORMATADA COM OS PRODUTOS E SEUS RESPECTIVOS PREÇOS, USANDO SOMENTE UMA TUPLA
prodprec = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 19.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99,
            'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('-' * 50)
print(f'{'LISTAGEM DE PREÇOS':^40}')
print('-' * 50)
for pos in range(0, len(prodprec)):
    if pos % 2 == 0:
        print(f'{prodprec[pos]:.<30}', end='')
    else:
        print(f'R${prodprec[pos]:>7.2f}')
print('-' * 50)
