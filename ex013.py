sal = float(input('Qual é o salário do funcionário? R$'))
aum = sal + (sal * 15 / 100)
print(f'Um funcionário que ganhava R${sal}, com 15% de aumento, passa a ganhar R${aum:.2f}')
