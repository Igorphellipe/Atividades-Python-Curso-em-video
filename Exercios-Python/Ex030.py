from time import sleep
print('------- Descobrindo Números PARES e IMPAR --------')
num = int(input('Digite um número para descobri se e PAR ou IMPAR ? '))
print('----- ANALISANDO O NÚMERO -----')
sleep(3)
if num % 2 == 0:
    print('O número {} é PAR!'.format(num))
else:
    print('O número {} é IMPAR!'.format(num))
print('------- FIM --------')
