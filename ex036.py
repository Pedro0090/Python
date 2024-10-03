# PROGRAMA PARA APROVAR EMPÉSTIMO BANCÁRIO
valorcasa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
tempo = int(input('Tempo em anos do finaciamento: '))
# AQUI ESTÁ A PRESTAÇÃO DA CASA E A PORCENTAGEM QUE CALCULA QUANTO É 30% SALÁRIO DO COMPRADOR
prestacao =  valorcasa / tempo / 12
porcentagem = salario * 0.3

# SE A PRESTAÇÃO FOR MAIOR QUE 30% DO SALÁRIO DO COMPRADOR NÃO SERÁ POSSÍVEL O EMPRÉSTIMO, CASO CONTRÁRIO O EMPRÉSTIMO
# É POSÍVEL
if prestacao <= porcentagem:
    print(f'Para pagar uma casa  no valor de R${valorcasa:.2f} em {tempo} anos a prestação será de R${prestacao:.2f}')
    print('Empréstimo APROVADO!')
else:
    print(f'Para pagar uma casa no valor de R${valorcasa:.2f} em {tempo} anos a prestação será de R${prestacao:.2f}')
    print('Empréstimo NEGADO!')
