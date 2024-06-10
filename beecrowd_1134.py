#TIPOS DE COMBUSTÍVEL

import os
os.system('cls')

alcohol = 0
gas = 0
diesel = 0
while True:
    fuel = int(input())
    if fuel == 4:
        break
    else:
        if fuel == 1:
            alcohol+=1
        elif fuel == 2:
            gas+=1
        elif fuel == 3:
            diesel+=1
print('MUITO OBRIGADO')
print(f'Alcool: {alcohol}')
print(f'Gasolina: {gas}')
print(f'Diesel: {diesel}')