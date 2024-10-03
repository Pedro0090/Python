# PROGRAMA QUE PEDE NÚMEROS E AO FINAL MOSTRA A LISTA COMPLETA, E DUAS OUTRAS LISTAS DIVIDIDAS ENTRE PARES E ÍMPARES
# lista = []
# listapar = []
# listaimpar = []
# while True:
#     valor = int(input('Digite um número: '))
#     lista.append(valor)
#     o = ' '
#     if valor % 2 == 0:
#         listapar.append(valor)
#     else:
#         listaimpar.append(valor)
#     while o not in 'SsNn':
#         o = input('Quer continuar? [S/N] ').strip()
#     if o in 'Nn':
#         break
# print('-=' * 30)
# print(f'A lista completa é: {lista}')
# print(f'A lista de pares é : {listapar}')
# print(f'A lista de ímpares é: {listaimpar}')

lista = []
listapar = []
listaimpar = []
while True:
    lista.append(int(input('Digite um número: ')))
    o = ' '
    while o not in 'SsNn':
        o = input('Quer continuar? [S/N] ').strip()
    if o in 'Nn':
        break
for v in lista:
    if v % 2 == 0:
        listapar.append(v)
    else:
        listaimpar.append(v)
print('-=' * 30)
print(f'A lista completa é: {lista}')
print(f'A lista de pares é : {listapar}')
print(f'A lista de ímpares é: {listaimpar}')
