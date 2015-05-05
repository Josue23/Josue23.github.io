
print('\nCalcula o valor do aluguel de um carro. ')

dia = int(input('\nQuantos dias: '))
km = float(input('Km rodados: '))

valorDias = dia * 60
valorKm = km * 0.15
total = valorDias + valorKm

print('\nTotal = R$ %.2f \n' %total)
