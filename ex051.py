# PROGRAMA QUE MOSTRA UMA PROGRESSÃO ARITMÉTICA
print('=' * 35)
print(f'{'10 TERMOS DE UMA PA':^10}')
print('=' * 35)
termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = termo + (10-1) * razao
for i in range(termo, decimo + razao, razao):
    print(f'{i}', end= ' → ')
print('FIM')
