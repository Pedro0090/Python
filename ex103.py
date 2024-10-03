def ficha(n='<desconhecido>', g=0):
    print(f'O jogador {n} fez {g} gol(s) no campeonato')


print('-' * 30)
nome = str(input('Nome do Jogador: ')).strip().title()
gols = str(input('Quantidade de gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome == '':
    ficha(g=gols)
else:
    ficha(n=nome, g=gols)
ficha()
