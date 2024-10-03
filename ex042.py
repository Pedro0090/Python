# PROGRAMA QUE DIZ SE AS RETAS PODEM FORMAR UM TRIÂNGULO E DIZ SE O TRIÂNGULO É ESCALENO, EQUILÁTERO OU ISÓSCELES
lado1 = float(input('Primeiro segmento: '))
lado2 = float(input('Segundo segmento: '))
lado3 = float(input('Terceiro segmento: '))
# FÓRMULA PARA SABER SE OS SEGUIMENTOS FORMAM UM TRIÂNGULO
'''tri = lado1 + lado2 > lado3 and lado1 + lado3 >lado2 and lado2 + lado3 > lado1
#FÓRMULA DOS TIPOS DE TRIÂNGULOS
iso = lado1 == lado2 or lado1 == lado3 or lado2 == lado3
eql = lado1 == lado2 == lado3
esc = lado1 != lado2 and lado1 != lado3 and lado2 != lado3

if tri == True and iso == True:
    print('Os segmentos acima PODEM FORMAR um triângulo ISÓSCELES!')
elif tri == True and eql == True:
    print('Os segmentos acima PODEM FORMAR um triângulo EQUILÁTERO!')
elif tri == True and esc == True:
    print('Os segmentos acima PODEM FORMAR um triângulo ESCALENO!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um TRIÂNGULO!')'''

if lado1 + lado2 > lado3 and lado1 + lado3 >lado2 and lado2 + lado3 > lado1:
    if lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print('Os segmentos acima PODEM FORMAR um triângulo ISÓSCELES!')
    elif lado1 == lado2 == lado3:
        print('Os segmentos acima PODEM FORMAR um triângulo EQUILÁTERO!')
    elif lado1 != lado2 !=lado3 != lado1:
        print('Os segmentos acima PODEM FORMAR um triângulo ESCALENO!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um TRIÂNGULO!')
