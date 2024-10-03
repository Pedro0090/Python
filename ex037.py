# PROGRAMA PARA CONVERTER NÚMERO INTEIRO PARA BINÁRIO, OCTAL OU HEXADECIMAL
num = int(input('Digite um número inteiro qualquer: '))
print('''Escolha uma opcão:
[1] Converter para BINÁRIO 
[2] Converter para OCTAL 
[3] Converter para HEXADECIMAL''')
escolha = int(input('Sua escolha: '))
if escolha == 1:
    b = bin(num)
    print(f'{num} convertido para BINÁRIO é {b[2:]}')
elif escolha == 2:
    o = oct(num)
    print(f'{num} convertido para OCTAL é {o[2:]}')
elif escolha == 3:
    h = hex(num)
    print(f'{num} convertido para HEXADECIMAL é {h[2:]}')
else:
    print('A opção escolhida é inválida!')
