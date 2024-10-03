# PROGRAMA QUE MOSTRA SE OS PARÊNTESES DA EXPRESSÃO DIGITADA ESTÃO VÁLIDOS
exp = str(input('Digite a expressão: '))
listexp = []
for s in exp:
    if s == '(':
        listexp.append('(')
    elif s == ')':
        if len(listexp) > 0:
            listexp.pop()
        else:
            listexp.append(')')
            break
if len(listexp) == 0:
    print('Sua epxressão está válida!')
else:
    print('Sua expressão está inválida!')
    