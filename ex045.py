# JOGO DE PEDRA PAPEL TESOURA (JOKENPO)
from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
print('''Escolha:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
pc = randint(0, 2)
usuario = int(input('Qual é a sua jogada? '))

if usuario == 0 or usuario == 1 or usuario == 2:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!')

    print('-=' * 11)
    print(f'Computador jogou {itens[pc]}')
    print(f'Jogador jogou {itens[usuario]}')
    print('-=' * 11)
    
    if pc == usuario:
        print('Empate!')
    elif pc == 0 and usuario == 1:
        print('Jogador ganhou!')
    elif pc == 0 and usuario == 2:
        print('Computador ganhou!')
    elif pc == 1 and usuario == 2:
        print('Computador ganhou!')
    elif pc == 1 and usuario == 0:
        print('Computador ganhou!')
    elif pc == 2 and usuario == 0:
        print('Jogador ganhou!')
    else:
        print('Jogador ganhou!')
else:
    print('Jogada Inválida!')
