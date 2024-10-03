# PROGRAMA QUE PEDE 7 VALORES E MOSTRA QUAIS SÃO OS PARES E ÍMPARES EM ORDEM, TENDO LISTAS DENTRO DE UMA LISTA
nums = [[], []]
for i in range(1, 8):
    n = int(input(f'Digite o {i}º valor: '))
    if n % 2 == 0:
        nums[0].append(n)
    else:
        nums[1].append(n)
nums[0].sort()
nums[1].sort()
print('-=' * 30)
print(f'Os valores pares digitados foram: {nums[0]}')
print(f'Os valores ímpares digitados foram: {nums[1]}')
