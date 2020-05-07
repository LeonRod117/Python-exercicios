from math import radians, sin, cos, tan
angulo = float(input('Informe o ângulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('Para o Ângulo {} graus temos os seguintes valores'.format(angulo))
print(' Seno é {:.2f} \n Cosseno é {:.2f} \n e Tangente é {:.2f}'.format(seno,cosseno,tangente))