
print('\nEste programa exibe o desconto de uma mercadoria. ')

preco = float(input('\nPreço: '))
porcentagem = float(input('Desconto: '))
desconto = preco / 100 * porcentagem

print('\nValor do desconto: R$ %.2f ' %desconto)
print('Total a pagar: R$ %.2f \n' %(preco - desconto))
