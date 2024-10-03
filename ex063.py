# SEQUÊNCIA DE FIBONACCI
print('-' * 35)
print('SEQUÊNCIA DE FIBONACCI')
print('-' * 35)
termos = int(input('Quantos termos você quer mostrar? '))
sequencia = 3
ptermo = 0
stermo = 1
print('~' * 30)
print(f'{ptermo} >> {stermo} >> ', end='')
while sequencia <= termos:
    ttermo = ptermo + stermo
    print(ttermo, end=' >> ')
    ptermo = stermo
    stermo = ttermo
    sequencia += 1
print('FIM')
