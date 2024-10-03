# PROGRAMA QUE MOSTRA O NÚMERO TIRADO POR 4 JOGADORES NO DADO E MOSTRA UM RANKING EM ORDEM DO MAIOR PARA O MENOR NÚMERO
from random import randint
from time import sleep

jgs = {
    'jogador1': randint(1, 6),
    'jogador2': randint(1, 6),
    'jogador3': randint(1, 6),
    'jogador4': randint(1, 6)
}
print('VALORES SORTEADOS:')
for k, v in jgs.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = [sorted(jgs.items(), key=lambda item: item[1], reverse=True)]
print('-=' * 30)
print('  == RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking, 1):
    print(f'  {i}º lugar: {v[0]} com {v[1]}')
    sleep(1)
