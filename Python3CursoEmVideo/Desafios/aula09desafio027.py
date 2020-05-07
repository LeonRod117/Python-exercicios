n = str(input('Digite seu nome completo: ')).strip()
nome = n.split() # Fatiamento da String N em vários blocos
print('Processando informações...')
print('Seu Primeiro nome é {}'.format(nome[0]))
print('Seu Último nome é {}'.format(nome[len(nome)-1])) # o len entra dentro da Lista do Split e é -1 para não contar a posição ZERO