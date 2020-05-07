import random
import time
dig = int(input('Informe seu número da sorte de 1 a 5: '))
num = random.randint(1,5)
print('Processando os dados...')
time.sleep(3) # dar um tempo para mostrar como se estivesse processando
print('O seu número da sorte é {}'.format(dig))
print('O numero sorteado foi {}'.format(num))
if num == dig:
    print('Parabéns !!! Vc acertou o número escolhido')
else:
    print('Não foi desta vez, tente novamente')
