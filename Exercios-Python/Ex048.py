print('\033[32m-=-\033[m' * 22)
print('\033[1;4mSOMA DE NÚMEROS IMPARES MULTIPLOS DE 3 DE 1 A 500\033[m')
print('\033[32m-=-\033[m' * 22)
s = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        s = s + c
print('A soma dos {} equivale a {} '.format(cont,s))
