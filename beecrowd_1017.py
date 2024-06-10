#GASTOS DE COMBUSTIVEL

import os
os.system('cls')

while True:
    try:
        time = int(input()) #informar o tempo gasto da viagem
        speed = int(input()) #informar a velocidade média
    except:
        print('write numbers')
    else:
        break
distance = speed*time
consume = distance/12 # 12km/l de consumo
print(f'{consume:.3f}')