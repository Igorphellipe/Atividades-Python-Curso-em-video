print('\033[31;4m------ Descobrindo um Trinagulo -------\033[m')
a = float(input('Digite um valor da reta 1: '))
b = float(input('Digite um valor da reta 2: '))
c = float(input('Digite um valor da reta 3: '))
print('-=-' * 20)
print('Analisando segmentos...')
print('-=-' * 20)
if a < b + c and b < a + c  and c < a + b:
    print('Os segmentos Formam um triangulo !')

else:
    print('Os segmentos não possibilitam criar um triangulo')

print('-----FIM-----')
