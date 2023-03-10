print('!!!!!!! Compre e ganhe desconto de até 5% !!!!!! \n')
valor = float(input('Digite o valor da compra: '))
desconto = valor - (valor * 0.05)
print('O do produto é R${:.2f}, com o desconto de 5% o valor total fica R${:.2f} !'.format(valor,desconto))
