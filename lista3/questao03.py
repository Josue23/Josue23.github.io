a = 80000
b = 200000
taxaA = a * (3/100)
taxaB = b * (1.5/100)
anos = 0
while a + taxaA <= b + taxaB:
	a = a * (1+(3/100))
	b = b * (1+(1.5/100))
	anos += 1
	print('\na ',a)
	print('b ',b)
	print(anos, 'anos \n')
print(anos, 'anos ')
