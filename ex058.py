# JOGO DE ADIVINHAÇÃO MELHORADO
from random import randint

print('-' * 50)
print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
print('-' * 50)
player = ''
pc = randint(0, 10)
tt = 0
while player != pc:
    tt += 1
    player = int(input('Tente: '))
    if pc > player:
        print('Errou kkk, tá mais alto...')
    elif pc < player:
        print('Errou kkk, tá mais baixo...')
print(f'Acertou com {tt} tentativas. Parabéns!')
