import random
lista = []
par = []
impar = []
n = 0
while len(lista) < 20:
	lista.append(random.randrange(1, 101))
	if lista[n] % 2 == 0:
		par.append(lista[n])
	else:
		impar.append(lista[n])
	n += 1
print('Lista: ', lista)
print('Par: ', par)
print('Impar: ', impar)
	
