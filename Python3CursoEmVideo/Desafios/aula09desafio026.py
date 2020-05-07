frase = str(input('Digite uma Frase: ')).strip() # Retira os espaços no início e fim
print('A Letra A aperece {} vezes'.format(frase.upper().count('A')))
print('A posição que ela aparece 1° vez é {}'.format(frase.upper().find('A')+1)) # +1 é para que não conte a posição ZERO
print('A posição que ela aparece por último é {}'.format(frase.upper().rfind('A')+1)) # + 1 é para que não conte a posição ZERO
