# PROGRAMA QUE IDENTIFICA SE O NOME TEM "SILVA"
name = str(input('Qual é seu nome completo: ')).upper().strip()
print(f'O seu nome tem Silva no nome ? {'SILVA' in name.split()}')
