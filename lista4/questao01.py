import random
lista = []
while len(lista) < 10:
    lista.append(random.randrange(1, 101))
lista.sort()
print('Menor valor: %s ' %lista[0])
print('Maior valor: %s ' %lista[9])
