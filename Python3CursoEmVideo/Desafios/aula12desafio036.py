# Desafio Financiamento Imobiliário
imovel = float(input('Informe o valor do imóvel: '))
salario = float(input('Qual seu salário mensal: '))
anos = int(input('Em quantos anos deseja o Financiamento:'))
meses = anos * 12
parcela = imovel / meses
print('\nConsiderando seu salário R$ {:.2f} e o valor do imóvel R$ {:.2f}\n'.format(salario, imovel))
if parcela >= salario - (salario * 70 / 100) and meses > 60:
    print('\033[1;31mSeu Financiamento não foi aprovado !!!\n'
          'as Parcelas R$ {:.2f} excedem 30% do seu salário R$ {:.2f}\n'.format(parcela, salario))
elif meses <= 60:
    print('\033[1;33m{} meses são insuficientes para Aprovação do Financiamento\n'
          'Tente simular com um número superior à 60 Parcelas\n'.format(meses))
else:
    print('\033[1;34mSeu Financiamento foi APROVADO !!!\n'
          'as Parcelas serão de R$ {:.2f} por mês, durante os {} Meses do contrato\n'.format(parcela, meses))
print('\033[1;36mMuito obrigado por escolher a nossa Imobiliária')


