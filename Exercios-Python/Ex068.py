from random import randint
print('\033[32m-=-\033[m' * 22)
print('                      \033[1;4mJOGO PAR OU IMPAR\033[m')
print('\033[32m-=-\033[m' * 22)
print('')
print('-=-' * 15)
print('VAMOS JOGAR PAR OU IMPAR')
print('-=-' * 15)
computador = randint(1, 10)
soma = 0
cont = 0
while True:
    jogador = int(input('Diga um valor: '))
    imp_par = str(input('Par ou Impar: ')).strip().upper()[0]
    print('==' * 22)
    soma = jogador + computador
    if soma % 2 == 0 and imp_par in 'Pp':
        print(f'Você jogou {jogador} e o computador {computador}. total de {soma} DEU PAR')
        print('==' * 22)
        print('Você ganhou!')
        print('Vamos jogar novamente...')
        print('==' * 22)
        cont = cont + 1
    if soma % 2 != 0 and imp_par in 'Ii':
        print(f'Você jogou {jogador} e o computador {computador}. Total de {soma} DEU IMPAR')
        print('==' * 22)
        print('Você ganhou!')
        print('Vamos jogar novamente...')
        print('==' * 22)
        cont = cont + 1
    if soma % 2 == 0 and imp_par in 'Ii':
        print(f'Você jogou {jogador} e o computador {computador}. total de {soma} DEU PAR')
        print('==' * 22)
        print('Você perdeu!')
        break
    if soma % 2 != 0 and imp_par in 'Pp':
        print(f'Você jogou {jogador} e o computador {computador}. total de {soma} DEU IMPAR')
        print('==' * 22)
        print('Você perdeu!')
        break
print('**' * 22)
print(f'GAME OVER! Você venceu {cont} vezes')





