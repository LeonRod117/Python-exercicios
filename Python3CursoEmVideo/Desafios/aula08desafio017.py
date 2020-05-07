from math import sqrt,pow
co = float(input('Informe o Cateto Oposto: '))
ca = float(input('Informe o Cateto Adjacente: '))
h = sqrt(pow(co,2)+pow(ca,2))   # Também poderia ser desta forma ==== ((co**2)+(ca**2))**(1/2) ====
print('O valor da Hipotenusa deste Triangulo é {:.2f}'.format(h))
