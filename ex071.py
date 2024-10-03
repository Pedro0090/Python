# CAIXA ELETRÔNICO COM CÉDULAS DE 50, 20, 10 E 1 REAL
print('='*40)
print(f'{'BANCO PDR':>23}')
print('='*40)
valor = int(input('Valor a ser sacado: R$'))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédula(s) de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('='*30)
print('Saque realizado com sucesso!')
