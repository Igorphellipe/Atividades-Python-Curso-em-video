from time import sleep
from random import randint
print('\033[32m-*-\033[m' * 22)
print('                             \033[1;4mJOGO JOKENPÔ\033[m')
print('\033[32m-*-\033[m' * 22)
print()
itens = ('Pedra','Papel','Tesoura')
computador = randint(0, 2)
print('\033[1mESCOLHA UMA DAS OPÇÕES\033[m')
print()
print('[0] PEDRA\n'
      '[1] PAPEL\n'
      '[2] TESOURA')
jogador = int(input('Qual número você escolhe: '))
print('JO')
sleep(1)
print('KEN')
sleep(2)
print('PÔ')
sleep(2)
print('\033[32m-*-\033[m' * 22)
print(f'Computador jogou: {itens[computador]}')
print(f'Jogador jogou: {itens[jogador]}')
print('\033[32m-*-\033[m' * 22)

#COMPUTADOR ESCOLHE PEDRA
if computador == 0:
      if jogador == 0:
            print('EMPATE !')

      elif jogador == 1:
                 print('JOGADOR VENCEU')

      elif jogador == 2:
                  print('COMPUTADOR VENCEU')
      else:
          print('JOGADA INVALIDA')

#COMPUTADOR ESCOLHE PAPEL
elif computador == 1:
      if jogador == 0:
            print('COMPUTADOR VENCEU')

      elif jogador == 1:
            print('EMPATE')

      elif jogador == 2:
           print('JOGADOR VENCEU')
      else:
          print('JOGADA INVALIDA')

#COMPUTADOR ESCOLHE TESOURA
elif computador == 2:
      if jogador == 0:
            print('JOGADOR VENCEU')

      elif jogador == 1:
            print('COMPUTADOR VENCEU')

      elif jogador == 2:
                  print('EMPATE')
      else:
          print('JOGADA INVALIDA')

print('\033[32m-*-\033[m' * 22)
