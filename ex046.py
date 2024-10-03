# PROGRAMA QUE MOSTRA UMA CONTAGEM DE 10 SEGUNDOS PARA QUEIMA DE FOGOS
from time import sleep

print('Os fogos serão em:')
sleep(1)
for contagem in range (10, -1, -1):
    print(f'{contagem}...')
    sleep(1)
print('FIIIIIIIIIIUUUU   BOOOOOOOOOOOOM   POOW   PÁÁ')
