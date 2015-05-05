
print('\nEste programa calcula quantos dias de vida um fumante perdeu. ')

cigarrosDia = int(input('\nCigarros fumados por dia: '))
anos = int(input('Quantos anos já fumou: '))

totalCigarros = (cigarrosDia * anos * 365) / 144

print('\nVocê perdeu %d dias de vida. \n' %totalCigarros)

