from time import sleep
print('\033[32m-=-\033[m' * 22)
print('                   \033[1;4mCALCULADORA DE IMC\033[m')
print('\033[32m-=-\033[m' * 22)
print('                   INDICE DE INTERPRETAÇÃO DO IMC')
print('IMC                     CLASSIFICAÇÃO              OBESIDADE(grau)\n'
      'MENOR QUE 18.5            MAGREZA                            0\n'
      'ENTRE 18.5 E 24.9         NORMAL                             0\n'
      'ENTRE 25.0 E 29.9         SOBREPESO                          I\n'
      'ENTRE 30.0 E 39.9         OBESIDADE                          II\n'
      'MAIOR QUE 40.0            OBESIDADE GRAVE                    III')
print('\033[32m-=-\033[m' * 22)
input('Pressione <> Enter ')
nome = str(input('Digite seu nome: '))
altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
print()
imc = peso / (altura ** 2)
print('\033[32m-=-\033[m' * 20)
print('                   \033[4mCALCULANDO\033[m')
print('\033[32m-=-\033[m' * 20)
sleep(3)

if imc < 18.5:
    print('Olá {}, seu IMC é {:.2f} nesse caso você está abaixo do peso,\n'
          'procure um nutricionista !'.format(nome, imc))

elif imc >= 18.5 and imc < 25.0:
    print('Olá {}, seu IMC é {:.2f} você está com peso ideal mantenha sempre assim !'.format(nome, imc))

elif imc >=25.1 and  imc < 30.0:
    print('Olá {}, seu IMC é {:.2f} você está sobrepeso procure exercita-se mais !'.format(nome, imc))

elif imc >=30.1 and imc < 40.0:
    print('Olá {}, seu IMC é {:.2f} você está obeso pedimos que procure um médico o mais breve! '.format(nome, imc))

elif imc >= 40.1:
    print('Olá {}, seu IMC é {:.2f} você está com obesidade morbida procure um médico com urgência !'.format(nome, imc))

print()
print('                              \033[4mSUA SAÚDE EM PRIMEIRO LUGAR\033[m')
