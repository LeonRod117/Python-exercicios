n1 = float(input('Quanto você tem em Reais na carteira: '))
usd = float(3.27)
conv = n1 / usd
print('Você possui {} Reais que Equivalem à {:.2f} Dólar(es)'.format(n1, conv))
