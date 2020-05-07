# Conversão de Bases Numéricas

num = int(input('Insira um número: '))
print('''Escolha uma das bases para conversão:
      [ 1 ] converter para BINÁRIO
      [ 2 ] converter para OCTAL
      [ 3 ] converter para HEXADECIMAL''')
opcao = int(input('Sua Opção: '))
if opcao == 1:
    print('\033[1;31m{} convertido para BINÁRIO é {}'.format(num,bin(num)[2:]))  #0b Binário
elif opcao == 2:
    print('\033[1;36m{} convertido para OCTAL é {}'.format(num, oct(num)[2:]))   #0o Octal
else:
    print('\033[1;35{} convertido para HEXADECIMAL é {}'.format(num, hex(num)[2:])) #0x Hexadecimal

# Usamos o Fatiamento com [2:] para Eliminar os 2 primeiros digitos dos valores apresentados
