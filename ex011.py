l = float(input('Largura da parede: '))
a = float(input('Altura da parede: '))
ar = l * a
t = ar / 2
print(f'Sua parede tem a dimensão de {l}x{a} e sua área é de {ar:.3f}m²')
print(f'Para pintar essa parede você vai precisar de {t:.4f}l de tinta')
