# PROGRAMA GERENCIADOR DE PAGAMENTOS
print(f'{"LOJAS PEDRÃO":=^40}')
preco = float(input('Preço das Compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] À VISTA (dinhero/cheque)
[ 2 ] À VISTA (cartão)   
[ 3 ] 2x NO CARTÃO
[ 4 ] 3X OU MAIS NO CARTÃO''')
escolha = int(input('Escolha uma opção: '))
if escolha == 1:
    total = preco - (preco * 0.15)
elif escolha == 2:
    total = preco - (preco * 0.5)
elif escolha == 3:
    total = preco / 2
    print(f'Sua compra será parcelada em 2x de R${total:.2f} SEM JUROS.')
elif escolha == 4:
    total = preco + (preco * 0.2)
    parcela = int(input('Informe quantas vezes quer pagar: x'))
    totalparcela = total / parcela
    print(f'Sua compra será parcelada em {parcela}x de R${totalparcela:.2f} COM JUROS.')
else:
    total = 0
    print('Opção inválida! Tente novamente.')
print(f'sua compra de R${preco:.2f} vai custar R${total:.2f} no final')
