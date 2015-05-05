x = 1
n = int(input('Numero: '))
while True:
	if x * (x+1) * (x+2) == n:
		print(('%d x %d x %d = %d ') %(x, x+1, x+2, n))
		print('%d e Triangular ' %n)
		break
	x += 1
