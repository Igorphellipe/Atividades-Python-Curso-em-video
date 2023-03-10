import math
print('------ Calculando a Hipotenusa -------')
cat_op = float(input('Digite o valor do Cateto Oposto: '))
cat_adj = float(input('Digite o valor do Catato adjacente: '))
soma = (cat_op ** 2) + (cat_adj ** 2)
hipotenusa = math.sqrt(soma)
print('O valor da hipotenusa é: {:.2f}'.format(hipotenusa))
