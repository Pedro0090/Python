# PROGRAMA QUE PEDE OS DADOS DE PESSOAS E MOSTRA UMA ANÁLISE DOS DADOS DIGITADOS
pessoas = {}
lista = []
m = 0
while True:
    pessoas['nome'] = str(input('Nome: ')).strip().title()
    while True:
        pessoas['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()
        if pessoas['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoas['idade'] = int(input('Idade: '))
    m += pessoas['idade']
    lista.append(pessoas.copy())
    while True:
        cont = str(input('Quer continuar ? [S/N] ')).strip()
        if cont in 'SsNn':
            break
        print('ERRO! Responda apenas S ou N.')
    if cont in 'Nn':
        break
print('-=' * 30)
p = len(lista)
media = m / p
print(f'A) Ao todo, temos {p} pessoa(s) cadastrada(s).')
print(f'B) A média de idade é de {media:.2f} anos.')
print('C) As mulheres cadastradas foram ', end='')
for i in lista:
    if i['sexo'] == 'F':
        print(i['nome'], end=' ')
print()
print('D) Lista das pessoas que estão acima da média:')
for p in lista:
    if p['idade'] >= media:
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')
