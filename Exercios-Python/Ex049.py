print('\033[32m-=-\033[m' * 22)
print('                      \033[1;4mDESCOBRINDO TABUADA\033[m')
print('\033[32m-=-\033[m' * 22)

n = int(input('Digite um número: '))
mult = 0
for c in range(0, 10+1):
    mult = n * c
    print('{} x {:2} = {}'.format(n, c, mult))
