def leiaint(x):
    ok = False
    valor = 0
    while True:
        p = str(input(x))
        if p.isnumeric():
            valor = int(p)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            return valor


n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
