# PROGAMA QUE PEDE NÚMEROS PARA UMA LISTA, NÃO ACEITA NÚMEROS REPETIDOS E NO FINAL MOSTRA DO MAIOR PARA O MAIOR VALOR
v = []
while True:
    vd = (input('Digite um valor: '))
    if vd in v:
        print('Valor duplicado! Não vou adicionar...')
    else:
        v.append(vd)
        print('Valor adicionado com sucesso...')
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N] ').upper().strip()
    if continuar == 'N':
        break
v.sort()
print(f'Você digitou os seguintes valores: {', '.join(v)}.')
