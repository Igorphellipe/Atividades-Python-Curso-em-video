from time import sleep
print('\033[32m-*-\033[m' * 20)
print('                   \033[1;4mESCOLA VIVER UM SONHO\033[m')
print('\033[32m-*-\033[m' * 20)
print()
print('\033[4mCONTROLE DE ALUNOS\033[m')

nome = str(input('Digite o nome do aluno: ')).title().strip()
nota1 = float(input('Digite o valor da nota do 1º Semestre: '))
nota2 = float(input('Digite o valor da nota do 2º Semestre: '))

media = (nota1 + nota2 ) / 2
print()
print('                      \033[4mCALCULANDO NOTAS\033[m')
sleep(3)
if media < 5.0:
    print('O aluno {}, obteve uma média de {}, estando reprovado! '.format(nome, media))
    print('Boas férias ! ')
elif media >= 5.0 and media <= 6.9:
    print('O aluno {}, obteve uma média de {}, ficando de recuperação! '.format(nome, media))
    print('Bons estudos! ')
elif media >= 7.0:
    print('O aluno {}, obteve exito com média {}, estando aprovado! '.format(nome, media))
    print('Parabéns e Boas ferias!')
print()
print('\033[32m-*-\033[m' * 20)
print('                   \033[1;4mESCOLA VIVER UM SONHO\033[m')
print('\033[32m-*-\033[m' * 20)
