
print('\nEste programa calcula o aumento de um salário. ')

salario = float(input('\nSalário: '))
porcentagem = float(input('Porcentagem de aumento: '))

aumento = salario * porcentagem / 100
novoSalario = salario + aumento

print('\nO valor do aumento é de R$ %.2f ' %aumento)
print('O valor do novo salário é R$ %.2f \n' %novoSalario)
