# PROGRAMA QUE MOSTRA ALGUMAS ESTATÍSTICAS SOBRE COMPRAS FEITAS
print('-'*40)
print(f'{'LOJAS SUPER BARATÃO':>25}')
print('-'*40)
soma = custmil = maisb = c = 0
nomemaisb = ''
while True:
    nome = str(input('Nome do produto: ')).strip().title()
    preco = float(input('Preço: R$'))
    contin = ' '
    while contin not in 'SN':
        contin = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    soma += preco
    if preco > 1000:
        custmil += 1
    c += 1
    if c == 1 or preco < maisb:
        maisb = preco
        nomemaisb = nome
    if contin == 'N':
        break
print(f'O total da compra foi R${soma:.2f}')
print(f'Temos {custmil} produto(s) custando mais de R$1000.00')
print(f'O produto mais barato foi o(a) {nomemaisb} que custa R${maisb:.2f}')
