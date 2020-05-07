salario = float(input('Informe o salário do funcionário em R$: '))
if salario > 1250.00:
    print('O Salário reajustado é de 10% R$: {:.2f}'.format((salario)+(salario*0.10)))
else:
    salario <= 1250.00
    print('O Salário reajustado é de 15% R$: {:.2f}'.format((salario)+(salario*0.15)))

### Solução do Professor abaixo

salario = float(input('Informe o valor do salário em R$: '))
if salario <= 1250.00:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('Seu salário de R$ {:.2f} foi reajustado para R$ {:.2f}'.format(salario, novo))