from time import sleep
from datetime import date
print('\033[32m-*-\033[m' * 20)
print('                   \033[1;4mCONSULTA ALISTAMENTO\033[m')
print('\033[32m-*-\033[m' * 20)
nome = str(input('Digite seu nome completo: ')).strip().upper()
nasc = int(input('Digite o ano de nascimento: '))
ano = date.today().year
idade = ano - nasc
print()
print('\033[32m-*-\033[m' * 20)
print('                    \033[1;4mVERIFICANDO DADOS\033[m')
print('\033[32m-*-\033[m' * 20)
sleep(3)
if  idade < 18:
    falta = 18 - idade
    alis = ano + falta
    print('Como vai {}, você ainda não tem idade para se alistar\n'
          'faltam {} ano(s) para seu alistamento!'.format(nome,falta))
    print('Seu alistamento será em {}'.format(alis))
elif ano - idade == 18:
    print('{}, Você completou 18 anos, já esta na hora de se alistar !'.format(nome))
elif idade > 18:
    passou =  idade - 18
    pas = ano - passou
    print('Olá {}, você passou {} ano(s) do periodo de alistamento !'.format(nome, passou))
    print('Seu ano de alistamento foi em {}'.format(pas))
    print('Por favor procure uma junta militar mais proxima ou entre no site:\n'
          '           \033[34mhttps://Alistamentomilitar.gov.br\033[m')

    print('Atenção caso tenha se alistado desconsiderar essa mensagem !')
print()
print('          \033[1;4mSISTEMA BRASILEIRO DE ALISTAMENTO AGRADECE A VISITA !\033[m')
