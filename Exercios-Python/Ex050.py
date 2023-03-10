print('\033[32m-=-\033[m' * 22)
print('                   \033[1;4mSOMA DE NÚMEROS PARES\033[m')
print('\033[32m-=-\033[m' * 22)
s = 0
cont = 0
for c in range(1, 7):
    n = int(input('Digite o {}º valor: '.format(c)))
    if n % 2 == 0:
        s = n + s
        cont = cont + 1
print('Você informou um total de {} números e a soma entre eles foi {}'. format(cont,s))
