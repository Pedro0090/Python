from math import radians, sin, cos, tan

a = float(input('Digite o ângulo que você deseja: '))
print(f'O ângulo de {a} tem o seno de {sin(radians(a)):.2f}')
print(f'O ângulo de {a} tem o cosseno de {cos(radians(a)):.2f}')
print(f'O ângulo de {a} tem a tangente de {tan(radians(a)):.2f}')
