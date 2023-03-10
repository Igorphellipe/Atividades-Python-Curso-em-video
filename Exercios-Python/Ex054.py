from datetime import date
print('\033[32m-=-\033[m' * 22)
print('                   \033[1;4mDESCOBRINDO MAIOR IDADE\033[m')
print('\033[32m-=-\033[m' * 22)
ano = date.today().year
cont = 0
cont_1 = 0
for c in range(0, 7):
    nascimento = int(input('Digite seu nascimento: '))
    if ano - nascimento >= 21:
        cont = cont + 1
    elif ano - nascimento < 21:
        cont_1 = cont_1 + 1
print('{} Pessoas atigiram ou passaram dos 21 anos !'.format(cont))
print('{} Pessoa(s) ainda não atingiram os 21 anos !'.format(cont_1))
