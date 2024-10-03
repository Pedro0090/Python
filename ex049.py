# PROGRAMA QUE MOSTRA A TABUADA DO 0 ATÉ O 10 DE UM NÚMERO DIGITADO
n = int(input('Digite um número para ver sua tabuada: '))
for c in range(0, 11):
    print(f'{n} x {c:2} = {n * c}')
