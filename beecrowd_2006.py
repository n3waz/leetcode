# IDENTIFICANDO O CHÁ

import os
os.system('cls')

cont = 0 
cha = int(input()) 
competidores = input().split() 

for i in range(len(competidores)):
    if int(competidores[i]) == cha:
        cont += 1
print(cont)