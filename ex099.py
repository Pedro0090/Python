# FUNÇÃO QUE DESCOBRE QUAL O MAIOR NÚMERO
def maior(*n):
    mai = 0
    # mai = max(n) caso não usar if else (if not use "if else")
    print('-=' * 30)
    print('Analisando os valores passados...')
    for i, v in enumerate(n):
        if i == 0:
            mai = v
        else:
            if mai < v:
                mai = v
        print(v, end=' ')
    print(f'Foram informados {len(n)} valores ao todo.')
    print(f'O maior valor informado foi {mai}.')


maior(5, 16, 2, 19, 55, 12)
maior(6, 7, 9)
maior(0, 3)
maior(1)
maior()
