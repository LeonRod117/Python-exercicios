from datetime import date
ano = int(input('Informe um Ano ? Coloque 0 para analisar o Ano Atual: '))
if ano == 0:
    ano = date.today().year #### Busca o ano atual da máquina
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O Ano {} é Bissexto'.format(ano))
else:
    print('O Ano {} Não é Bissexto'.format(ano))

