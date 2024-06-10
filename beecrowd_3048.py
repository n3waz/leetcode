# # SEQUÊNCIA SECRETA

import os
os.system('cls')

sequencia = [] # lista vazia
tamanho = int(input()) # tamanho da lista
os.system('cls')

for i in range(tamanho): # para cada elemento da lista
    num = int(input()) # recebe o elemento
    if not sequencia: # se a lista estiver vazia
        sequencia.append(num) # adiciona o elemento
    elif num != sequencia[-1]: # se o elemento for diferente do ultimo elemento da lista
        sequencia.append(num) # adiciona o elemento
print(len(sequencia)) # imprime o tamanho da lista