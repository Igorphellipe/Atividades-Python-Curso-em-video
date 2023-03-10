from random import randint
print('\033[32m-*-\033[m' * 22)
print('                   \033[1;4mJOGO DA ADVINHAÇÃO 2.0\033[m')
print('\033[32m-*-\033[m' * 22)
computador = randint (0, 10)
num = 0
cont = 0
print('Olá, vamos jogar! ')
while num != computador:
    num = int(input('Vamos lá em que número estou pensando: '))
    cont = cont + 1
    if num == computador:
        print('Parabens você acertou, após {} tentativa(s)'.format(cont))
    else:
        if num < computador:
            print('Mais... Tente mais uma vez! ')
        elif num > computador:
            print('Menos... Tente mais uma vez!')
print('O computador escolheu o Número {} !'.format(computador))
print('FIM')