#QUADRADO DE PARES
import os
os.system('cls')
while True:
    try:
        num = int(input()) #valor inteiro N
    except:
        print('Only numbers')
    else:
        break

for i in range(1, num+1): #num assume o range como index
    if i % 2 == 0:
        square = i*i
        print(f'{i}^2 = {square}')
    else:
        pass