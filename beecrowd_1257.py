import os
os.system("cls")

lista = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4,
         'F':5, 'G':6, 'H':7, 'I':8, 'J':9, 'K':10,
         'L':11, 'M':12, 'N':13, 'O':14, 'P':15,
         'Q':16, 'R':17, 'S':18, 'T':19, 'U':20,
         'V':21, 'W':22, 'X':23, 'Y':24, 'Z':25  }

testes = int(input())
valor = 0

for casos in range(testes):
    cont = 0
    valor = 0
    L = int(input())

    for i in range(L):
        frase = input().upper()
        frase = list(frase)

        for j in range(len(frase)):
            valor += lista[frase[j]] + cont + j
    
        cont+=1
    print(valor)