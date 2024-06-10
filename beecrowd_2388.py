# TACÓGRAFO

import os
os.system('cls')

n = int(input()) 
total = 0
for i in range(n):
    t, v = map(int,input().split())
    total += t*v
print(total)
