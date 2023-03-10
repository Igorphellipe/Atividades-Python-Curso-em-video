print('\033[34m-*-\033[m' * 22)
print('                  \033[1;4mDESCOBRINDO NÚMEROS PRIMO\033[m')
print('\033[34m-*-\033[m' * 22)

num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[31m', end='')
        tot = tot + 1
    else:
        print('\033[32m', end='')
    print('{} '.format(c), end='')
if tot == 2:
    print('\n\033[mÉ um número primo')
else:
    print('\n\033[mNão é um número primo')






