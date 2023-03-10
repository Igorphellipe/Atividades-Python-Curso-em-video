from time import sleep
print('\033[32m-=-\033[m' * 20)
print('                \033[4mFINANCIAMENTO BANCÁRIO\033[m')
print('\033[32m-=-\033[m' * 20)
valor_casa = float(input('Informe o valor do imovél: R$'))
prazo_pagamento = int(input('Informe o prazo para pagamento: '))
salario = float(input('Informe sua renda mensal: R$'))
meses = prazo_pagamento * 12
prestaçao = valor_casa / meses
salario_30 = salario * 0.3
print('\033[32m-=-\033[m' * 20)
print('                 \033[4mANALISANDO DADOS\033[m')
print('\033[32m-=-\033[m' * 20)
sleep(3)
if salario_30 >= prestaçao:
    print('Proposta de Crédito aprovada!')
    print('Valor do financiamento: R${}'.format(valor_casa))
    print('Prazo para pagamento {} meses'.format(meses))
    print('Valor da prestação R${:.2f}'.format(prestaçao))
    print('Para concluir o financiamento dirija-se até uma agência Banco de Todos !')
elif salario_30 < prestaçao:
    print('Proposta de Crédito negada!')
    print('Tente um valor menor')
print()
print('                  \033[4;34mO Banco de Todos agradece a sua visita !!!\033[m')