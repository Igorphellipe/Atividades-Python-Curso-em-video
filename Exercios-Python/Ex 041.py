from time import sleep
from datetime import date
print('\033[32m-+-\033[m' * 30)
print('                   \033[1;4mCONFEDERAÇÃO DISTRITAL DE NATAÇÃO\033[m')
print('\033[32m-+-\033[m' * 30)

print('Bem vindo ao sistema de cadastro de Atletas de Natação, aqui formamos o futuro \n'
      'das piscinas do Brasil e estamos felizes pela sua visita !')
sleep(10)
print()
print()
print('\033[32m-*-\033[m' * 30)
print('                   \033[1;4mCADASTRO DE NOVOS ATLETAS\033[m')
print('\033[32m-*-\033[m' * 30)

nome = str(input('Digite seu nome completo: ')).strip().title()
nascimento = int(input('Digite o ano de nascimento: '))

ano = date.today().year
idade = ano - nascimento
print()
print()
print('\033[32m-**-\033[m' * 30)
print('                    \033[4mANALISANDO CADASTRO\033[m')
print('\033[32m-**-\033[m' * 30)
sleep(3)
if idade <= 9:
      print('Olá {}, sua idade é {} ano(s), e você foi matriculado na Turma \033[1mMIRIM\033[m.'.format(nome, idade))

elif idade >= 10 and idade <= 14:
      print('Olá {}, sua idade é {} ano(s), e você foi matriculado na Turma \033[1mINFANTIL\033[m.'.format(nome, idade))

elif idade >= 15 and idade <= 19:
      print('Olá {}, sua idade é {} ano(s), e você foi matriculado na Turma \033[1mJUNIOR\033[m.'.format(nome, idade))

elif idade == 20:
      print('Olá {}, sua idade é {} ano(s), e você foi matriculado na Turma \033[1mSÊNIOR\033[m.'.format(nome, idade))

elif idade > 20:
      print('Olá {}, sua idade é {} ano(s), e você foi matriculado na turma \033[1mMASTER\033[m.'.format(nome, idade))

print('Seja bem vindo, estamos anciosos para começarmos a treinar !')

print('                     \033[1;4mCONFEDERAÇÃO DISTRITAL DE NATAÇÃO\033[m')
