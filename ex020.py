from random import sample
from shlex import join

a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')
lista = sample([a1, a2, a3, a4], k=4)
print(f'A ordem de apresentação do trabalho será {', '.join(lista)}')
