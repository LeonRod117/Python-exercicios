vel = int(input('Informe Velocidade Medida: '))
lim = int(80)
multa = float(7)
valor = (vel-80)*multa
print('Velocidade considerada de {} KM/h'.format(vel))
if vel > lim:
    print('Seu veículo foi Multado !!!')
    print('O valor de sua Multa é R${:.2f}'.format(valor))
else:
    print('Boa Viajem !!!')
