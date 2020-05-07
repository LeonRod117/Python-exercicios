nome = str(input('Digite seu Nome Completo: ')).strip() #tira os espaços no começo e fim
print('Seu nome está sendo processado...')
print('Seu nome em MAIÚSCULAS é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} Letras'.format(len(nome) - nome.count(' '))) #retira os espaços do meio
separa = nome.split()
print('Seu Primeiro Nome é {} e tem {} Letras'.format(separa[0],len(separa[0])))

