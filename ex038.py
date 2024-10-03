# PROGRAMA QUE DIZ DENTRE DOIS NÚMEROS QUAL É MAIOR ou SE OS DOIS SÃO IGUAIS
n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
if n1 > n2:
    print(f'O PRIMEIRO VALOR é MAIOR.')
elif n1 < n2:
    print(f'O SEGUNDO VALOR é MAIOR.')
else:
    print(f'Os valores digitados são IGUAIS.')
