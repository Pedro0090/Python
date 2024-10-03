# PROGRAMA COM MENU BÁSICO
from time import sleep

v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))
o = ''
while o != 5:
    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair''')
    o = int(input('>>>> Sua opção: '))
    if o == 1:
        print(f'A soma entre {v1} e {v2} é {v1+v2}')
    elif o == 2:
        print(f'O produto de {v1} e {v2} é {v1*v2}')
    elif o == 3:
        if v1 > v2:
            print(f'Entre {v1} e {v2} o maior valor é {v1}.')
        elif v1 < v2:
            print(f'Entre {v1} e {v2} o maior valor é {v2}')
        else:
            print('Os dois valores digitados são iguais!')
    elif o == 4:
        print('Informe os números denovo.')
        v1 = int(input('Primeiro valor: '))
        v2 = int(input('Segundo valor: '))
    elif o == 5:
        print('Aguarde...')
        sleep(1)
    else:
        print('Opção inválida, tente novamente!')
    print('=' * 40)
    sleep(2)
print('Fim do programa!')
