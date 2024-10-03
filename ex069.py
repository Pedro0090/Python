# PROGRAMA DE CADASTRO DE PESSOAS COM INFORMAÇÕES AO FINAL DA EXECUÇÃO DO PROGRAMA
maior18 = h = m = 0
while True:
    sexo = ' '
    cont = ' '
    print('-'*30)
    print(f'{'CADASTRE UMA PESSOA':>21}')
    print('-'*30)
    idade = int(input('Idade: '))
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        maior18 += 1
    if sexo == 'M':
        h += 1
    if sexo in 'F' and idade < 20:
        m += 1
    while cont not in 'SN':
        cont = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if cont == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {maior18}')
print(f'Ao todo temos {h} homens cadastrados.')
print(f'Temos também {m} mulheres com menos de 20 anos.')
