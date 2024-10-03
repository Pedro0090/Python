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


def leiareal(x):
    while True:
        try:
            p = float(input(x))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Por favor digite um número real válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[0;31mO usuário decidiu não digitar esse número.\033[m')
            return 0
        else:
            return p


n = leiaint('Digite um número inteiro: ')
r = leiareal('Digite um número real: ')
print(f'O valor inteiro digitado foi {n} e o real foi {r}')
