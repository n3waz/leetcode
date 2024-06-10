#O MAIOR
import math
import os
os.system('cls')

while True:
    try:
        valor = input().split(" ")
        a, b, c = valor

        maior = (int(a) + int(b) + abs(int(a) - int(b)))  / 2
        resultado = (int(maior) + int(c) + abs(int(maior) - int(c)))/2
    except:
        continue
    else:
        print("%d eh o maior" %resultado) #%d serve para marcar posição de um número inteiro
        break