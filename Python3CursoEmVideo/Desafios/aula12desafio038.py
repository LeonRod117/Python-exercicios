n1 = int(input('Insira o 1° Valor: '))
n2 = int(input('Insira o 2° Valor: '))
print('Analisando os números {} e {}\n'.format(n1, n2))
print('Podemos concluir que...')
if n1 > n2:
    print('O primeiro valor {} é Maior que {}'.format(n1, n2))
elif n2 > n1:
    print('O segundo valor {} é Maior que {}'.format(n2, n1))
else:
    print('Não existe valor maior os dois são Iguais')