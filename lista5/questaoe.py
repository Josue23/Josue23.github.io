
numero= []
n = 0
while len(numero) < 6:
	p = int(input('Numero: '))	
	while numero[p]==numero[p-1]:
		print('Digite um numero diferente de %d ' %numero[p])
		p = int(input('Numero: '))
	numero.append(p)
	if numero[0]!= numero[n-1] and sum(numero)%2 == 0:
		print(numero)
		n += 1

'''
numero= []
n = 0
while len(numero) < 6:
	p = int(input('Numero: '))
	while numero[p]==numero[p-1]:
		print('Digite um numero diferente de %d ' %numero[p])
		p = int(input('Numero: '))
	numero.append(p)
	n += 1
	if numero[0]!= numero[n-1] and numero[n]!= numero[n+1] and sum(numero)%2 == 0:
		print(numero)

'''
