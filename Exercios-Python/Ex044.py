from time import sleep
print('\033[32m-*-\033[m' * 22)
print('                     \033[1;4mLOJAS PETROPOLIS\033[m')
print('\033[32m-*-\033[m' * 22)
print()
print('                     \033[4mCAIXA LIVRE\033[m')
print()
cliente = str(input('Digite o nome do cliente: ')).strip().title()
produto = str(input('Digite o nome do produto: ')).strip().upper()
valor = float(input('Digite o valor do produto R$: '))
print()
sleep(3)
print('\033[32m-=-\033[m' * 22)
print('                     \033[1mESCOLHA UMA FORMA DE PAGAMENTO\033[m')
print('\033[32m-=-\033[m' * 22)

pagamento = int(input('[1] para pagamento À vista Dinheiro/Cheque 10% desconto \n'
      '[2] para pagamento À vista no Cartão de Crédito 5% desconto \n'
      '[3] para pagamento Parcelado em 2x no Cartão de Crédito sem desconto \n'
      '[4] para pagamento Parcelado em 3x ou mais no Cartão de Crédito 20% Juros\n'
                      'DIGITE UMA OPÇÃO:'))

print()
print('\033[32m-=-\033[m' * 22)
print('                     \033[1mFINALIZANDO COMPRA EMITINDO CUPOM DE VENDA\033[m')
print('\033[32m-=-\033[m' * 22)

if pagamento == 1:
    valor_10 =  valor - (valor * 0.10)
    print('Pagamento à vista {}, receberá 10% de desconto\n'
          'o valor de R${:.2f} ficará R${:.2f} '.format(produto, valor, valor_10))
elif pagamento == 2:
    valor_5 =  valor -(valor * 0.05)
    print('Pagamento à vista no cartão {}, receberá 5% de desconto\n'
          'o valor de R${:.2f} ficara R${:.2f}'.format(produto, valor, valor_5))
elif pagamento == 3:
    valor_div = valor / 2
    print('Pagamento parcelado no cartão {}, em 2x de R${:.2f}, com total de R${:.2f}'.format(produto, valor_div, valor))

elif pagamento == 4:
    parcelas = float(input('Quantas parcelas? '))
    valor_20 = (valor * 0.20) + valor
    valor_3x = valor_20 / parcelas
    print('Pagamento parcelado no cartão {}, em 3X ou mais fica com 20% de Juros\n'
          'o valor das parcelas ficam em R${:.2f}, o valor total e R${:.2f} e com juros fica {:.2f}'.format(produto,valor_3x, valor, valor_20))
print('Cliente {}:'.format(cliente))
print('Produto {}:'.format(produto))
print('                      \033[1;4mLOJAS PETROPOLIS AGRADECE A PREFERÊNCIA\033[m')
