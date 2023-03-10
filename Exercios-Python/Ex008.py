print('Olá, Bem vindo ao conversor de Medidas! \n')

n1 = float(input('Digite um valor para conversão: '))
km  = n1 / 1000
hm  = n1 / 100
dam = n1 / 10
dm = n1 * 10
cm = n1 * 100
mm = n1 * 1000

print('O valor de {:.2f}m correspode a: '.format(n1))
print('{}km'.format(km))
print('{}hm'.format(hm))
print('{}dam'.format(dam))
print('{}dm'.format(dm))
print('{}cm'.format(cm))
print('{}mm'.format(mm))