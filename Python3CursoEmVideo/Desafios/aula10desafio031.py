km = int(input('Informe a Distância da Viajem em KM: '))
tar1 = km * 0.50
tar2 = km * 0.45
print('Para esta viajem de {} KM'.format(km))
if km <= 200:
    print('Tarifa da Passagem R${:.2f}'.format(tar1))
else:
    print('Tarifa da Passagem RS{:.2f}'.format(tar2))
print('Uma Boa Viajem !!!')
