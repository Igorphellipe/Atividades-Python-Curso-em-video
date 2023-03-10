print('\033[32m-=-\033[m' * 22)
print('                     \033[1;4CALCULANDO VALORES !\033[m')
print('\033[32m-=-\033[m' * 22)
cont = 0
soma = 0
n = 0
n = int(input('Digite um valor / 999 para parar: '))
while n != 999:
    soma = soma + n
    cont = cont + 1
    n = int(input('Digite um valor / 999 para parar: '))
print('Você digitou {} Número(s):'.format(cont))
print('A soma entre eles é {}'.format(soma))