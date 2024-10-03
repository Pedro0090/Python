sal = float(input('Digite o salário do funcionário: R$'))
if sal <= 1250:
    novosal = sal + (sal * 15 / 100)
else:
    novosal = sal + (sal * 10 / 100)
print(f'Quem ganhava R${sal} passa a ganhar R${novosal:.2f}')
