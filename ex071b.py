# CAIXA ELETRÔNICO COM CÉDULAS DE 50, 20, 10 E 1 REAL (OUTRA MANEIRA DE FAZER)
print('='*40)
print(f'{'BANCO PDR':>23}')
print('='*40)
valor = int(input('Valor a ser sacado: R$'))
ced50 = valor // 50
ced20 = (valor - ced50 * 50) // 20
ced10 = (valor - ced50 * 50 - ced20 * 20) // 10
ced1 = valor - ced50 * 50 - ced20 * 20 - ced10 * 10
if ced50 > 0:
    print(f'Total de {ced50} cédula(s) de R$50.00')
if ced20 > 0:
    print(f'Total de {ced20} cédula(s) de R$20.00')
if ced10 > 0:
    print(f'Total de {ced10} cédula(s) de R$10.00')
if ced1> 0:
    print(f'Total de {ced1} cédula(s) de R$1.00')
print('='*30)
print('Saque realizado com sucesso!')
