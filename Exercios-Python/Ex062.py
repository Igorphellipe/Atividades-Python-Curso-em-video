print('\033[32m-=-\033[m' * 22)
print('                     \033[1;4mGERADOR DE PA 2ª PARTE\033[m')
print('\033[32m-=-\033[m' * 22)
p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
termo = p
cont = 1
mais = 10
total = 0
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo = termo + r
        cont = cont + 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais: '))
print('Sua progressão finalizou com {} termos mostrados!'.format(total))
print('fim')