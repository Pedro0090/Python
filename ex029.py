from time import sleep


vel = float(input('Qual é a velocidade atual do carro? '))
multa = (vel - 80) * 7 # Como o limite é de 80 km, basta tirar -80 do total da velocidade, e o que sobrar multiplica-se
# pelo valor da multa

sleep(2)

# Estrutura de repertição para saber se o carro foi multado ou não
if vel <= 80:
    print('\033[34mTenha um bom dia e dirija com segurança!\033[m')
else:
    print('\033[31mMULTADO! Você excedeu o limite permitido que é de 80km/h!')
    print(f'\033[31mVocê deve pagar uma multa de R${multa:.2f}\033[m')
