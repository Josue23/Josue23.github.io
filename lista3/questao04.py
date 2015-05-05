a, b = 1, 1
k = 1
fib = int(input('Digite um numero: '))
while k <= fib-2:
	a, b = b, a+b
	k += 1
print(b)
