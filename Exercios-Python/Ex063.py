print('\033[32m-\033[m' * 55)
print('            \033[1;4mSEQUÊNCIA DE FIBONACCI\033[m')
print('\033[32m-\033[m' * 55)
termo = int(input('Quantos Termos você quer mostrar: '))
t1 = 0
t2 = 1
print('*' * 35)
print('{} -> {}'.format(t1, t2), end='')
cont = 3
while cont <= termo:
    t3 = t1 + t2
    print(' -> {} '.format(t3), end='')
    cont = cont + 1
    t1 = t2
    t2 = t3
print(' -> fim')
print('*-*' * 35)

