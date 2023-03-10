from datetime import date
print('\033[34;4m-------- Descobrindo Anos BISSEXTO -------------\033[m')
ano = int(input('Digite um ano para analisar ? ou digite 0 para o ano atual? '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de {} é Bissexto !'.format(ano))
else:
    print('O ano de {} não e Bissexto !'.format(ano))