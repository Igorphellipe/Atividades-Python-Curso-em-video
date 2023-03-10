from random import randint
from time import sleep
print('------ Jogo de Advinhação -------')
num1 = int(input('Digite um número entre 0 e 5: '))
sorteio = randint(0, 5)
print('sorteando número !!!')
sleep(3)
if num1 == sorteio:
    print('Parabéns você acertou!! ')
else:
    print('Não foi dessa vez Tente Novamente !!')
print('----- Fim -----')
print('O Número correto é {}'.format(sorteio))



