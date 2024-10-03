# PROGRAMA QUE PEDE ALGUNS DADOS, AOS QUAIS SÃO RETORNADOS DE FORMA DIDÁTICA
jogadores = []
jogador = {}
gol = []
while True:
    jogador['nome'] = str(input('Nome do jogador: ')).strip().title()
    part = int(input(f'Quantas partidas {jogador['nome']} jogou? '))
    for p in range(1, part+1):
        gol.append(int(input(f'Quantos gols na partida {p}? ')))
    jogador['gols'] = gol[:]
    jogador['total'] = sum(gol)
    gol.clear()
    jogadores.append(jogador.copy())
    cont = ' '
    while cont not in 'SsNn':
        cont = input('Quer continuar? [S/N] ').strip()
        if cont not in 'SsNn':
            print('ERRO! Responda apenas com S ou N')
    if cont in 'Nn':
        break
print('-=' * 30)
print(f'cod', end=' ')
for i in jogador.keys():
    print(f'{i:<13}', end='')
print()
print('-' * 40)
for k, v in enumerate(jogadores):
    print(f'{k:>3} ', end='')
    for j in v.values():
        print(f'{str(j):<13}', end='')
    print()
while True:
    print('-' * 40)
    d = int(input('Mostrar dados de qual jogador? (999 para parar): '))
    if d == 999:
        break
    while True:
        if d < (len(jogadores) + 1):
            print(f'-- Levantamento do jogador {jogadores[d]['nome']}:')
            for i, g in enumerate(jogadores[d]['gols'], 1):
                print(f'   Na partida {i} fez {g} gols.')
            break
        else:
            print(f'ERRO! Não existe jogador de código {d}.')
            break
print('<< FINALIZADO >>')
