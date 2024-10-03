# PROGRAMA QUE PEDE VALORES E AO FIM DO LAÇO INFORMA QUANTOS NÚMEROS FORAM DIGITADOS E A SOMA ENTRE ELES (999 NÃO CONTA)
qn = soma = 0
n = int(input('Digite um número [999 para parar]: '))
while n != 999:
    soma += n
    qn += 1
    n = int(input('Digite um número [999 para parar]: '))
print(f'Você digitou {qn} número(s) e a soma foi {soma}.')
