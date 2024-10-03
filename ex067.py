# PROGRAMA QUE PEDE UM NÚMERO,S MOSTRA SUA TABUADA E SÓ PARA QUANDO O NÚMERO DIGITADO FOR NEGATIVO
while True:
    n = int(input('Digite um número para ver sua tabuada: '))
    print('-' * 30)
    if n < 0:
        break
    for t in range(1, 11):
        print(f'{n} x {t:2} = {n * t}')
    print('-' * 30)
print('PROGRAMA ENCERRADO COM SUCESSO!')
