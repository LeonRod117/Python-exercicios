from random import shuffle
n1 = str(input('Digite o 1 Aluno: '))
n2 = str(input('Digite o 2 Aluno: '))
n3 = str(input('Digite o 3 Aluno: '))
n4 = str(input('Digite o 4 Aluno: '))
lista = [n1,n2,n3,n4]
shuffle(lista)
print('A Ordem de Apresentação será: ')
print(lista)
