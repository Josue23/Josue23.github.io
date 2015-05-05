peso = float(input('Quilos de peixe: '))
if peso > 50:
	excesso = peso - 50
	multa = excesso * 4
	print('\nJoao deve pagar R$ %.2f de multa. ' %multa)
else:
	print('\nExcesso = zero ')
	print('Multa = zero ')
