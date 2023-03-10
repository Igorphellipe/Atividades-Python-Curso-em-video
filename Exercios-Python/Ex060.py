#CALCULANDO O FATORIAL COM WHILE
print('\033[32m-+-\033[m' * 22)
print('                        \033[1;4mFATORANDO NÚMEROS\033[m')
print('\033[32m-+-\033[m' * 22)
num = int(input('Digite um valor: '))
c = num
f = 1
print('Calculando {}! = '.format(num), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f = f * c
    c = c - 1
print('{}'.format(f))

#Fatorial usando laço FOR
n = int(input('Digite um valor para calcular seu Fatorial: '))
print('Calcualndo o {}! = '.format(n),end='')
f = 1
for c in range(n, 0, -1):
    print('{}'.format(c),end='')
    print(' x ' if c > 1 else ' = ', end='')
    f = f * c
print(f)