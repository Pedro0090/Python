p = float(input('Qual é o preço do produto? R$'))
por = p * 5 / 100
print(f'O produto que valia R${p}, na promoção por 5% de desconto vai custar R${p - por:.2f}')
