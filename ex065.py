# PROGRAMA QUE PEDE NÚMEROS E MOSTRA INFORMAÇÕES COMO MENOR, MAIOR, MÉDIA E TOTAL DIGITADO
media = cont = soma = maior = menor = 0
r = 'S'
while r in 'Ss':
    n = int(input('Digite um número: '))
    r = str(input('Quer continuar? [S/N] ')).strip()[0]
    cont += 1
    soma += n
    if cont == 1:
        maior = n
        menor = n
    else:
        if maior < n:
            maior = n
        if menor > n:
            menor = n
media = soma / cont
print(f'Você digitou {cont} número(s) e a média foi de {media:.2f}')
print(f'O maior valor foi de {maior} e o menor valor foi de {menor}')
