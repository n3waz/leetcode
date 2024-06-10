#AREA DO CIRCULO

import os
os.system('cls')

while True:
    try:
        radius = float(input()) # entrada do raio
        num_pi = 3.14159
        area = num_pi*(radius*radius)
    except:
        continue
    else:
        print(f'A={area:.4f}')
        break