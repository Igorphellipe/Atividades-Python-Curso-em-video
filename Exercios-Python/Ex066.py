print('\033[32m-=-\033[m' * 22)
print('                        \033[1;4mSOMANDO VALORES\033[m')
print('\033[32m-=-\033[m' * 22)
soma = 0
cont = 0
while True:
    n = int(input('Digite um valor [999 para sair]: '))
    if n == 999:
        break
    soma = soma + n
    cont = cont + 1
print(f'Você digitou {cont} números e a soma total entre eles é {soma}')
