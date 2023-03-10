import math
print('--------- Trigonometria -----------')
valor = float(input('Digite um valor: '))
cosseno = math.cos(math.radians(valor))
seno = math.sin(math.radians(valor))
tangente = math.tan(math.radians(valor))
print('O seno de {} será {:.2f}'.format(valor,seno))
print('O cosseno de {} será {:.2f}'.format(valor,cosseno))
print('A tangente de {} será {:.2f}'.format(valor,tangente))
