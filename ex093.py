# PROGRAMA QUE MOSTRA ESTATÍSTICAS DO JOGADOR COM OS DADOS DIGITADOS
jogador = {}
gol = []
jogador['nome'] = str(input('Nome do Jogador: ')).strip()
partidas = int(input(f'Quantas partidas {jogador['nome']} jogou? '))
for g in range(1, partidas + 1):
    gol.append(int(input(f'   Quantos gols na partida {g}? ')))
jogador['gols'] = gol[:]
jogador['total'] = sum(gol)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'{k} é {v}')
print('-=' * 30)
print(f'O jogador {jogador['nome']} jogou {len[gol]} partidas.')
for i, v in enumerate(jogador[gol], 1):
    print(f' => Na partida {i}, fez {v} gol(s).')
print(f'Foi um total de {jogador['total']} gol(s).')
