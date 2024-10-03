# PROGRAMA QUE CALCULA O IMC DE UMA PESSOA E INFORMA SEU ESTADO
peso = float(input('Informe o peso (KG): '))
altura = float(input('Informe a altura (M): '))

# CALCULO DO IMC
imc = peso / pow(altura, 2)

if imc < 18.5:
    print(f'O imc da pessoa informada é {imc:.2f}')
    print('Essa pessoa está ABAIXO DO PESO NORMAL!')
elif imc < 25:
    print(f'O imc da pessoa informada é {imc:.2f}')
    print('Essa pessoa está NA FAIXA NORMAL!')
elif imc < 30:
    print(f'O imc da pessoa informada é {imc:.2f}')
    print('Essa pessoa está EM SOBREPESO!')
elif imc < 40:
    print(f'O imc da pessoa informada é {imc:.2f}')
    print('Essa pessoa está EM OBESIDADE!')
else:
    print(f'O imc da pessoa informada é {imc:.2f}')
    print('Essa pessoa está EM OBESIDADE MÓRBIDA!')
