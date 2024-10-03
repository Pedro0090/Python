# PROGRAMA QUE CALCULA A ÁREA DE UM TERRENO ATRAVES DA FUNÇÃO area()
def area(x, y):
    a = x * y
    print(f'A área de um terreno {x}x{y} é de {a}m².')


print('Controle de Terrenos')
print('-' * 20)
larg = float(input('LARGURA (m): '))
comp = (float(input('COMPRIMENTO (c): ')))
area(x=larg, y=comp)
