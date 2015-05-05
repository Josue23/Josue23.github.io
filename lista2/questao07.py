metros = float(input('Metros: '))
latas = metros/54
preco = 80
if metros % 54 != 0:
	latas += 1
print('%d lata(s)' %latas)
print('Total R$ %.2f ' %(int(latas) * preco))
