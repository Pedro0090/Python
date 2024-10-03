# JOGO QUE PAR OU ÍMPAR CONTRA O COMPUTADOR (SÓ PARA QUANDO O JOGADOR PERDER)
from random import randint


print('-=-' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-=-' * 20)
v = 0
while True:
    pc = randint(0, 10)
    human = int(input('Diga um valor: '))
    parouimpar = ' '
    while parouimpar not in 'PI':
        parouimpar = str(input('Par ou Ímpar ? [P/I] ')).upper().strip()[0]
    print('-' * 30)
    soma = human + pc
    print(f'Você jogou {human} e o computador {pc}. O total de {soma} é ', end='')
    print('PAR' if soma % 2 == 0 else 'IMPAR')
    if soma % 2 == 0 and parouimpar == 'P':
        print('-' * 30)
        print('Você venceu!')
        print('-' * 30)
        print('Vamos jogar novamente...')
        v += 1
        print('-=-' * 20)
    elif soma % 2 != 0 and parouimpar == 'I':
        print('-' * 30)
        print('Você venceu!')
        print('-' * 30)
        print('Vamos jogar novamente...')
        v += 1
        print('-=-' * 20)
    elif soma % 2 == 0 and parouimpar == 'I':
        print('-' * 30)
        print('VOCÊ PERDEU !')
        print('-=-' * 20)
        break
    else:
        print('-' * 30)
        print('VOCÊ PERDEU !')
        print('-=-' * 20)
        break
print(f'GAME OVER! Você venceu {v} vezes.')
