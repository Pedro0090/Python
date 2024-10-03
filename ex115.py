from ex115m.lib.interface import *
from ex115m.lib.arquivo import *
from time import sleep


arq = 'arquivo.txt'

if not arqexiste(arq):
    criararq(arq)

while True:
    resp = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])
    if resp == 1:
        cabec('PESSOAS CADASTRADAS')
        sleep(0.6)
        lerarq(arq)
        sleep(5)
    elif resp == 2:
        cabec('NOVO CADASTRO')
        nome = str(input('Nome: ')).strip().title()
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resp == 3:
        cabec('Saindo do sistema... Até logo!')
        sleep(1.2)
        break
    else:
        print('\033[0;31mERRO! Digite uma opção válida!.\033[m')
        sleep(2)
