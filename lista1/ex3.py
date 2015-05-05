print('\nEste programa ler a qtde de dias, horas, minutos e segundos de um usuário e exibe o total de segundos. ')

dias = int(input('\nDias: '))
horas = int(input('Horas: '))
minutos = int(input('Minutos: '))
segundos = int(input('Segundos: '))

totalSegundos = (dias * 24 * 60 * 60) + (horas * 60 * 60) + (minutos * 60) + segundos

print('\n%d dia(s), %d hora(s), %d minuto(s), %d segundo(s) equivale a %d segundo(s). \n' %(dias, horas, minutos, segundos, totalSegundos))
