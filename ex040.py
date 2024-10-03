# PROGRAMA PARA SABER SE O ALUNO FOI APROVADO, FOI REPROVADO OU ESTÁ DE RECUPERAÇÃO PELA MÉDIA DE DUAS NOTAS
nota1 = float(input('Digite a nota do aluno: '))
nota2 = float(input('Digite a outra nota do aluno: '))
media = (nota1 + nota2) / 2

# SE A MÉDIA FOR MENOR QUE 5 O ALUNO ESTÁ REPROVADO. SE A MÉDIA ESTIVER ENTRE 5 E 6,9 ESTÁ DE RECUPERAÇÃO, CASO
# CONTRÁRIO O ALUNO PASOU
if media < 5:
    print(f'O aluno foi reprovado com pontuação média de {media:.1f} pontos.')
elif 7 > media >= 5:
    print(f'O aluno está de recuperaçao com uma pontuação média de {media:.1f} pontos.')
else:
    print(f'O aluno está aprovado com uma pontuação média de {media:.1f} pontos.')
