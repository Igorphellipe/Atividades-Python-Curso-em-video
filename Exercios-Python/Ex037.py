from time import sleep
print('\033[32m-=-\033[m' * 20)
print('             \033[4mTRANSFORMANDO NÚMEROS\033[m      ')
print('\033[32m-=-\033[m' * 20)
num = int(input('Digite um número: '))
escolha = int(input('ESCOLHA UMA DAS OPÇÕES\n'
                    'Digite 1 para conversão binaria\n'
                    'Digite 2 para conversão octal\n'
                    'Digite 3 para conversão hexadecimal\n'
                    'sua opção: '))
print('\033[32m-=-\033[m' * 20)
print('            \033[4mPROCESSANDO\033[m ')
print('\033[32m-=-\033[m' * 20)
sleep(3)
if escolha == 1:
    print('O número {} convertido em binario é {} !'.format(num, bin(num)[2:]))

elif escolha == 2:
    print('O número {} convertido em octal é {} !'.format(num, oct(num)[2:]))

elif escolha == 3:

    print('O número {} convertido em hexadecimal é {} !'.format(num, hex(num)[2:]))

else:
    print('\033[31mNenhuma das opções foi escolhida tente novamente!!\033[m')
print('\033[32m-=-\033[m' * 20)
print('                FIM')
print('\033[32m-=-\033[m' * 20)