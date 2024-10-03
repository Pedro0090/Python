"""city = str(input('Em qual cidade você nasceu: ')).strip()
print(city[:5].upper() == 'SANTO')"""

city = str(input('Em qual cidade você nasceu: ')).strip().upper()
print('SANTO' in city.split())
