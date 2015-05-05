
print('\nEste programa calcula o tempo de uma viagem de carro. ')

distancia = float(input('\nDistância: '))
velocidade = float(input('Velocidade média: '))
tempo = distancia / velocidade

if tempo * 60 >= 60:
    print('\nO tempo da viagem é %.2f hora(s). \n' %(tempo * 60 / 60))
else:
    print('\nO tempo da viagem é %d minutos.\n' %(tempo * 60))
