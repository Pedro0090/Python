# PROGRAMA QUE FAZ UMA FORMATAÇÃO EM UMA FRASE PARA QUE ELA SE ADEQUE
def formatacao(msg):
    t = len(msg) + 4
    print('~' * t)
    print(f'  {msg}')
    print('~' * t)


frase = str(input('Digite sua frase: '))
formatacao(frase)
