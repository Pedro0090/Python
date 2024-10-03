# PROGRAMA QUE MOSTRA UM BOLETIM ESCOLAR COM MÉDIA E ALGUMAS INFORMAÇÕES (PARTE VISUAL PÍFIA -_- )
from time import sleep


temp = []
bol = []
while True: 
    name = str(input('Nome: ')).split()
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    bol.append([name, [n1, n2], media])
    cont = ' '
    while cont not in 'SsNn':
        cont = input('Quer continuar? [S/N] ').strip()
    if cont in 'Nn':
        break
print('-=' * 30)
print(f'{'N°':<4}{'Nome':<10}{'Média':>8}')
print('-' * 26)
for i, a in enumerate(bol):
    print(f'{i:<4} {a[0]}{a[2]:>8.1f}')
while True:
    print('-' * 35)
    o = int(input('Mostrar notas de qual aluno? (999 interrompe) '))
    if o == 999:
        break
    if o <= len(bol) - 1:
        print(f'Notas de {bol[o][0]} são: {bol[o][1]}')
print('Finalizando...')
sleep(2)
print('<< Programa finalizado com sucesso >>')
