# PROGRAMA QUE PEDE ALGUNS NÚMEROS, ARMAZENA DENTRO DE UMA LISTA E AO FINAL MOSTRA ALGUMAS INFORMAÇÕES SOBRE A LISTA
lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    o = ' '
    while o not in 'SN':
        o = input('Quer continuar? [S/N] ').strip().upper()
    if o == 'N':
        break
lista.sort(reverse=True)
print('-=' * 30)
print(f'Você digitou {len(lista)} elementos.')
print(f'Os valores em ordem decrescente são: {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
