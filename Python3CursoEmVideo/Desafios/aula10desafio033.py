a = int(input('Digite o 1° valor: '))
b = int(input('Digite o 2° valor: '))
c = int(input('Digite o 3° valor: '))
### Verificando quem é o menor
menor = a
if b < c and b < a:
    menor = b
if c < a and c < b:
    menor = c
### Verificando quem é o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))

