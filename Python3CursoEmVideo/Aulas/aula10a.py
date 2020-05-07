n1 = float(input('Insira a Nota 1: '))
n2 = float(input('Insira a Nota 2: '))
m = (n1+n2)/2
print('A média das notas é {:.1f}'.format(m))
if m >= 6.0:
    print('Sua média está boa')
else:
    print('Sua média está baixa')

