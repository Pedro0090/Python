# PROGRMA QUE PEGA OS DADOS DE 4 PESSOAS, E MOSTRA ALGUNS DADOS ANALISADOS
media = 0
mvelho = 0
nomemvelho = ''
mulheres = 0
for p in range(1, 5):
    print(f'{f" {p}ª PESSOA ":-^20}')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    media += idade
    if p == 1 and sexo in "Mm":
        mvelho = idade
        nomemvelho = nome
    if idade > mvelho and sexo in "Mm":
        mvelho = idade
        nomemvelho = nome
    if sexo in "Ff" and idade < 20:
        mulheres += 1
print(f'A média de idade do grupo é {media / 4:.1f} anos.')
print(f'O homem mais velho tem {mvelho} anos e se chama {nomemvelho.title()}.')
print(f'Ao todo há {mulheres} mulher(es) com menos de 20 anos.')
