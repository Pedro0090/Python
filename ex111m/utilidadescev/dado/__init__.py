def leiadinheiro(x):
    while True:
        d = str(input(x)).strip()
        if d.replace(',', '').replace('.', '').isnumeric():
            if d.replace(',', '.') == float:
                return float(d.replace(',', '.'))
            else:
                print(f'\033[0;31mERRO: "{d}" é um preço inválido!\033[m')
        else:
            print(f'\033[0;31mERRO: "{d}" é um preço inválido!\033[m')
