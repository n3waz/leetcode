# DISTANCIA

import os 
os.system('cls')

while True:
    try:
        tempo = int(input())
        distancia = tempo * 2
    except:
        continue
    else:    
        print(distancia, "minutos")
        break