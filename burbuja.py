import random
def ordenamientoBurbuja(unaLista):
    for numPasada in range(len(unaLista)-1,0,-1):
        for i in range(numPasada):
            if unaLista[i]>unaLista[i+1]:
                temp = unaLista[i]
                unaLista[i] = unaLista[i+1]
                unaLista[i+1] = temp


#lista generada aleatoriamente
mi_lista = random.sample(range(100), 10)
print("Lista original desordenada: ",mi_lista)
#Se ordena con la funcion ordenamientoBurbuja
ordenamientoBurbuja(mi_lista)
print("Lista ordenada: ",mi_lista)
