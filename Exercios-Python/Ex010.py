print('!!! Bem vindo ao conversor de moedas !!!\n')

n1 = float(input('Digite um valor para converção em R$'))
con = n1/5.08
print('Com o seu valor de R${:.2f}, você pode comprar US${:.2f} Dólares.'.format(n1,con))