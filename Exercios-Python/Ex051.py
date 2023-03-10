print('\033[34m-*-\033[m' * 22)
print('                  \033[1;4mPROGRESSÃO ARITIMETICA\033[m')
print('\033[34m-*-\033[m' * 22)

p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
decimo = p + (10 - 1) * r
for c in range(p, decimo + r, r):
    print('{}'.format(c),end=' -> ')
print('Acabadou!')
