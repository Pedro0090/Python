# PROGRAMA QUE PEDE 5 NÚMEROS E OS COLOCA EM ORDEM SEM USAR O SORT
valores = []
for i in range(0, 5):
    valor = int(input('Digite um valor: '))
    if i == 0 or valor > valores[-1]:
        valores.append(valor)
        print('Valor adicionado ao final da lista...')
    else:
        p = 0
        while p < len(valores):
            if valor <= valores[p]:
                valores.insert(p, valor)
                print(f'Valor adicionado na posição {p} da lista...')
                break
            p += 1
print(f'Os valores digitados em ordem foram: {valores}')
