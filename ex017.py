'''from math import sqrt

cto = float(input('Comprimento do cateto oposto: '))
cta = float(input('Comprimento do cateto adjascente: '))

print(f'A hipotenusa vai medir {sqrt((cto**2)+(cta**2)):.2f}')'''

from math import hypot

cto = float(input('Comprimento do cateto oposto: '))
cta = float(input('Comprimento do cateto adjascente: '))
hi = hypot(cto, cta)

print(f'A hipotenusa vai medir {hi:.2f}')
