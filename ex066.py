# PROGRAMA QUE PEDE NÚMEROS, MOSTRA QUANTOS FORAM DIGITADOS E A SOMA ENTRE ELES
cont = soma = 0
while True:
    n = int(input('Digite um número (999 para parar): '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'Foram digitados {cont} números e a soma entre eles é {soma}')
