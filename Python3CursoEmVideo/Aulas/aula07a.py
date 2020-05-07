n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro: '))
s = n1 + n2   #Soma
m = n1 * n2   #Multiplicação
d = n1 / n2   #Divisão
di = n1 // n2 #Divisão Inteira
e = n1 ** n2  #Exponênciação
print('A Soma é {} o Produto é {} e a Divisão é {:.3f}'.format(s, m, d), end= ' >>> ')
print('A Divisão Inteira é {} e a Potência é {}'.format(di, e))
