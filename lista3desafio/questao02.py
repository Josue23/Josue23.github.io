conta = int(input('Valor da conta: '))
pago = int(input('Valor pago: '))
troco = pago - conta
n = 0
soma = 0
notas = [50, 20, 10, 5, 2, 1]
while troco <= notas[n]:
	n += 1
	soma += 1
	
	

if troco > notas[0]:
	print(notas[0])
