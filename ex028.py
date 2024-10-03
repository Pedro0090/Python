from random import randint
from time import sleep

np = randint(0, 5)    # Gera um número random de 0 a 5
print('\033[34m-=\033[m' * 30)
print('\033[33mTente adivinhar o número que estou pensando de 0 a 5...\033[m')
print('\033[34m-=\033[m' * 30)
adv = int(input('Em que número eu pensei? '))    # INPUT para o jogador tentar adivinhar o número
print('\033[32mPROCESSANDO...\033[m')
sleep(3)
# Estrutura de reptição para saber se o computador ganhou ou não.
if adv == np:
    print(f'Parabéns, também pensei no número {np}')
else:
    print(f'KKK, pensei no número {np} e não no número {adv}. GANHEI!')
