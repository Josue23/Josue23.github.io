
print('\nEste programa converte de Fahrenheit para Celsius. ')

f = float(input('\nDigite em Fahrenheit: '))
#c = 9 / 5 * f - 32
c = (f - 32) / (9 / 5)

print('\n%.2fºF = %.2fºC \n' %(f, c))
