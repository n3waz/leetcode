#PARES E IMPARES

import os
os.system('cls')

pares = []
impares = []

num = int(input())
for i in range(num):
    numbers = int(input())
    if numbers % 2 == 0:
        pares.append(numbers)
    else:
        impares.append(numbers)
os.system('cls')
pares.sort()
impares.sort(reverse=True) #reverter os impares
for i in pares:
    print(i)
for i in impares:
    print(i)