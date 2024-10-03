# PROGRAMA PARA VER QUANTAS LETRAS "A" TEM NA FRASE, QUAL A POSIÇÃO DA PRIMEIRA E DA ÚLTIMA
frase = str(input('Digite uma frase: ')).upper().strip()
frase = frase.replace('Á', 'A')
frase = frase.replace('Ã', 'A')
frase = frase.replace('Â', 'A')
frase = frase.replace('À', 'A')
frase = frase.split()
frase = ''.join(frase)

print(f'A letra A aparece {frase.count('A')} vezes na frase.')
print(f'A primeira letra A apareceu na posição {frase.find('A') + 1}')
print(f'A última letra A apareceu na posição {frase.rfind('A') + 1}')
