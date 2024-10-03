# PROGRAMA QUE PEGA O PESO DE 5 PESSOAS, MOSTRA QUAL O MAIOR E QUAL O MENOR PESO
maiorpeso = 0
menorpeso = 0
for p in range(1, 6):
    peso = float(input(f'Peso da {p}ª pessoa: '))
    if p == 1:
        maiorpeso = peso
        menorpeso = peso
    else:
        if peso > maiorpeso:
            maiorpeso = peso
        if peso < menorpeso:
            menorpeso = peso
print(f'O maior peso lido foi de {maiorpeso}Kg')
print(f'O menor peso lido foi de {menorpeso}Kg')
