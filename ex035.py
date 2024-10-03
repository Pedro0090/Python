print('-=' * 30)
print('Analisador de Triângulos')
print('-=' * 30)
l1 = float(input('Primeiro Segmento: '))
l2 = float(input('Segundo Segmento: '))
l3 = float(input('Terceiro Segmento: '))
if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    print('Os segmentos acima PODEM FORMAR um triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')
