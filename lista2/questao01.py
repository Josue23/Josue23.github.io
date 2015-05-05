lado1 = float(input('Digite o lado 1: '))
lado2 = float(input('Digite o lado 2: '))
lado3 = float(input('Digite o lado 3: '))
if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
	if lado1 == lado2 == lado3:
		print('\nTriangulo equilatero. ')
	elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
		print('\nTriangulo isosceles. ')
	elif lado1 != lado2 != lado3:
		print('\nTriangulo escaleno. ')
else:
	print('\nAs tres medidas nao formam  um triangulo. ')
