# QUANTA MANDIOCA?

import os
os.system('cls')

mandioca = [300, 1500, 600, 1000, 150]
total = 0

for i in range(5): 
    total += mandioca[i] * int(input()) # 5 inputs
print(total + 225) 