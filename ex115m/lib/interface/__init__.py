def leiaint(x):
    while True:
        try:
            p = int(input(x))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Por favor digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[0;31mO usuário decidiu não digitar esse número.\033[m')
            return 0
        else:
            return p


def linha(t=42):
    return '-' * t


def cabec(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lst):
    cabec('MENU PRINCIPAL')
    c = 1
    for i in lst:
        print(f'\033[33m{c}\033[m - \033[34m{i}\033[m')
        c += 1
    print(linha())
    opc = leiaint('\033[32mSua opção\033[m: ')
    return opc
