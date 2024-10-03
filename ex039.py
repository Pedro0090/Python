# PROGRAMA PARA LER O ANO DE NASCIMENTO DE UM JOVEM E FALAR SE VAI SERVIR, JÁ PASSOU DO TEMPO OU AINDA NÃO ESTÁ NA HORA
#TAMBÉM DIZ SE PRECISA SERVIR A DEPENDER DO GÊNERO
from datetime import date

anonasc = int(input('Digite o ano do seu nascimento: '))
genero = int(input('\nDiga seu gênero: \n[1] Masculino \n[2] Feminino \n[3] Outro \n'))
anoatual = date.today().year
idade = anoatual - anonasc

if genero == 1:
    if idade < 18:
        print(f'Quem nasceu em {anonasc} tem {idade} anos em {anoatual}.')
        print(f'Ainda falta(m) {18 - idade} ano(s) para o alistamento militar obrigatório!')
        print(f'Seu alistamento será em {anonasc + 18}.')
    elif idade == 18:
        print(f'Quem nasceu em {anonasc} já tem {idade} anos em {anoatual}.')
        print('Está na hora de se alistar!')
    else:
        print(f'Quem nasceu em {anonasc} já tem {idade} anos em {anoatual}.')
        print(f'Você já deveria ter se alistado a {idade - 18} ano(s).')
        print(f'Seu alistamento foi em {anonasc + 18}.')
elif genero == 2:
    print('Como se trata de uma pessoa do gênero feminino você não precisa se alistar!')
elif genero == 3:
    print('Procure saber mais informações com o órgão responsável!')
else:
    print('Opção INVÁLIDA!')
