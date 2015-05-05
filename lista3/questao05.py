a = int(input('Numero a: '))
b = int(input('Numero b: '))
while a % b != 0:
	a, b = b, a%b
print(b)
