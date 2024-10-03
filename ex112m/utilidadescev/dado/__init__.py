def leiadinheiro(x):
    while True:
        d = str(input(x)).strip()
        if d.replace(',', '').replace('.', '').isnumeric():
            return float(d.replace(',', '.'))
        print(f'\033[0;31mERRO: "{d}" é um preço inválido!\033[m')
