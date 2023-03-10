from time import sleep
print('\033[34m-=-\033[m' * 20)
print('                 \033[4;1mCOMPARANDO NÚMEROS ENTRE SI\033[m')
print('\033[34m-=-\033[m' * 20)
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
print('\033[33m-¨-\033[m' * 20)
print('                    \033[4mPROCESSANDO\033[m')
print('\033[33m-¨-\033[m' * 20)
sleep(3)
if num1 > num2:
    print('O primeiro valor é maior {} > {}!'.format(num1, num2))
elif num2 > num1:
    print('O segundo valor é maior {} > {}!'.format(num2, num1))
elif num1 == num2:
    print('Não exites valor maior, os dois são iguais {} = {}'.format(num1, num2))
print()
print('\033[34m-=-\033[m' * 20)
print('                              FIM')
print('\033[34m-=-\033[m' * 20)