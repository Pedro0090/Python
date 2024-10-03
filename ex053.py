# PROGRAMA QUE MOSTRA SE UMA FRASE É PALÍNDROMA OU NÃO
frase = str(input('Digite uma frase: ')).upper().strip()
palavras = frase.split()
junto = ''.join(palavras)
'''inverso ='' '''
inverso = junto[::-1]
'''for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]'''
print(f'O inverso de {junto} é {inverso}.')
if inverso == junto:
    print('A frase digitada é um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
