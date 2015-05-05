nome = input('Nome: ')
senha = input('Senha: ')
while nome == senha:
	print('\nA senha deve ser diferente do nome. ')
	print('Por favor, digite novamente. ')
	nome = input('Nome: ')
	senha = input('Senha: ')
