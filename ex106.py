from time import sleep

cor = ['\033[m',          # 0 sem cor
       '\033[0;37;41m',   # 1 vermelho
       '\033[0;37;42m',   # 2 verde
       '\033[0;37;43m',   # 3 amarelo
       '\033[0;37;44m',   # 4 azul
       '\033[0;37;45m',   # 5 roxo
       '\033[0;30;107m']  # 6 branco]


def titulo(t, c=0):
    tam = len(t) + 4
    print(cor[c], end='')
    print('~' * tam)
    print(f'  {t}')
    print('~' * tam)
    print(cor[0], end='')
    sleep(1)


def ajuda(comand):
    titulo(f'Acessando manual do comando \'{comand}\'', 4)
    print(cor[6], end='')
    help(comand)
    print(cor[0], end='')
    sleep(0.5)


while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    h = str(input('Função ou Biblioteca > '))
    if h.upper() == 'FIM':
        break
    else:
        ajuda(h)
titulo('ATÉ LOGO!', 1)
