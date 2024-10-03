# PROGRAMA QUE MOSTRA A SOMA DE TODOS OS NÚMEROS ÍMPARES DE 1 A 500 MÚLTIPLOS DE 3
s = 0
cont = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        cont += 1
        s += c
print(f'A soma de todos os {cont} valores foi igual a {s}')
