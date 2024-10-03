# PROGRAMA QUE PEGA O NOME DE UM ALUNO, SUA MÉDIA, E MOSTRA SEUS DADOS. UTILIZAÇÃO DE DICIONÁRIOS
aluno = {}
aluno['nome'] = input('Nome: ').strip().title()
aluno['media'] = float(input(f'Média de {aluno['nome']}: '))
print('-=' * 20)
if aluno['media'] >= 7:
    aluno['situação'] = 'APROVADO(A)'
elif 5 <= aluno['media'] < 7:
    aluno['situação'] = 'RECUPERAÇÃO'
else:
    aluno['situação'] = 'REPROVADO(A)'
for k, v in aluno.items():
    print(f'  - {k} é {v}')
    