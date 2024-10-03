d = float(input('Qual é a distância da sua viagem? '))
print(f'Você está prester a começar uma viagem de {d:.2f}!')

if d <= 200:
    p1 = d * 0.50
    print(f'O preço da viagem será de R${p1:.2f}')
else:
    p2 = d * 0.45
    print(f'O preço da viagem será de R${p2:.2f}')

'''preço = d * 0.50 if <=200 else d * 0.45
print (f'O preço da vigem será de R${preço:.2f})'''