# PROGRAMA QUE SÓ ACEITA MASCULINO OU FEMININO COMO DADO VÁLIDO
s = str(input('Informe seu sexo: [M/F] ')).upper().strip()[0]
while s not in 'MF':
    s = str(input('Dado inválido. Por favor, informe seu sexo: [M/F] ')).upper()
print(f'Sexo {s} registrado com sucesso!')
