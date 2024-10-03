# PROGRAMA QUE FALA SOBRE OS TIMES NO BRASILEIRÃO(2024) COM TUPLA
times = ('Botafogo', 'Flamengo', 'Bahia', 'São Paulo', 'Athletico-PR', 'Atlético-MG', 'Bragantino', 'Palmeiras',
         'Internacional', 'Cruzeiro', 'Fortaleza', 'Juventude', 'Grêmio', 'Vasco', 'Corinthians', 'Fluminense',
         'Criciúma', 'Atlético-GO', 'Cuiabá', 'Vitória')
print('-=' * 30)
print(f'Lista de times do Brasileirão: {times}')
print('-=' * 30)
print(f'Os 5 primeiros são: {times[:5]}')
print('-=' * 30)
print(f'Os 4 últimos são: {times[-4:]}')
print('-=' * 30)
print(f'Os times em ordem alfabética: {sorted(times)}')
print('-=' * 30)
print(f'O Palmeiras está na {times.index('Palmeiras') + 1}º posição.')
