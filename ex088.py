# PROGRAMA QUE DÁ PALPITES PARA QUANTOS JOGOS DE MEGA SENA O USUÁRIO PEDIR
from random import randint
from time import sleep


jg = []
jogos = []
sor = tot = 0
print('-' * 30)
print(f'{'JOGUE NA MEGA SENA':^30}')
print('-' * 30)
q = int(input('Quantidade de jogos que desejas para serem sorteados: '))
for p in range(0, q):
    sor = 0
    while True:
        s = randint(1, 60)
        if s not in jogos:
            jogos.append(s)
            sor += 1
        if sor >= 6:
            break
    jogos.sort()
    jg.append(jogos[:])
    jogos.clear()
sleep(0.5)
print('-=' * 3, f'SORTEANDO {q} JOGOS', '-=' * 3)
for i, j in enumerate(jg, 1):
    sleep(1)
    print(f'Jogo {i}: {j}')
print('-=' * 5, '< BOA SORTE >', '-=' * 5)
