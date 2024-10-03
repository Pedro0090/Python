# PROGRAMA QUE LÊ UM NÚMERO POR EXTENSO SE DIGITADO DE UM A VINTE
numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze',
           'Treze', 'Quatorze ou Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    n = int(input('Digite um número de 0 a 20: '))
    if 0 <= n <= 20:
        print(f'Você digitou o número {numeros[n]}')
        o = str(input('Você quer digitar outro? [S/N] ')).strip().upper()[0]
        if o == 'N':
            break
    else:
        print('Tente novamente.', end=' ')
print('Programa finalizado!')
