# Condições Aninhadas

nome = str(input('Olá, Qual é o seu nome ? '))
if nome == 'Leonardo':
    print('Que Nome bonito')
elif nome == 'Paulo' or nome == 'Maria' or nome == 'Pedro':
    print('Seu nome é bem popular no Brasil')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome Feminino')
else:                                           # Poderíamos deixar sem a condição else sem nenhum problema
    print('Seu nome é bem normal')
print('Tenha um bom dia {}'.format(nome))
