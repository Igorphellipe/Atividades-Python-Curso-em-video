from time import sleep
print(' ------- Aplicador de Multas --------')
km = int(input('Digite o Km aferido: '))
placa = str(input('Digite o Número da Placa: '))
modelo = str(input('Modelo do Veiculo: ')).upper()
multa = float(km - 80) * 7
print(' Verificando dados ')
sleep(3)
if km > 80:
    print('Olá, você foi multado por excesso de velocidade !!')
    print('Veiculo: {}'.format(modelo))
    print('Placa: {}'.format(placa))
    print('O valor total da multa R$:{} '.format(multa))
    print('Velocidade aferida {} KM/H '.format(km))
else:
    print('O Veiculo {}, Placa {}, não possui multas por velocidade'.format(modelo,placa))
print('---- FIM CONSULTA ----')
