# PROGRAMA QUE LÊ 6 NÚMEROS E MOSTRA A SOMA DOS PARES, DESCARTANDO OS ÍMPARES
s = 0
cont = 0
for numeros in range(1, 7):
    n = int(input(f'Digite o {numeros}° valor: '))
    if n % 2 == 0:
        cont += 1   # cont = cont + 1
        s += n      # s = s + n
print(f'A soma dos {cont} pares digitados foi {s}')
