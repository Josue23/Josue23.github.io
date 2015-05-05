ano = int(input('Digite o ano: '))
if ano % 4 == 0 and ano % 100 != 0  or ano % 400 == 0:
	print('O ano %s e bissexto. ' %ano)
else:
	print('O ano %s nao e bissexto. ' %ano)
