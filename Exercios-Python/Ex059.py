from time import sleep
print('\033[32m-*-\033[m' * 22)
print('                    \033[1;4mSISTEMA BASICO DE CALCULOS\033[m')
print('\033[32m-*-\033[m' * 22)

num1 = int(input('Digite o 1º valor: '))
num2 = int(input('Digite o 2º valor: '))
opçao = 0
print('                     \033[1;4mEscolha uma das opções\033[m')
print('\033[32m---\033[m' * 22)
while opçao != 5:
    opçao = int(input('\n[1] SOMAR\n'
                      '[2] MULTIPLICAR\n'
                      '[3] MAIOR\n'
                      '[4] NOVOS NÚMEROS\n'
                      '[5] SAIR DO PROGRAMA\n'
                      'Digite uma Opção: '))

    #Opção de Soma
    if opçao == 1:
        soma = num1 + num2
        print('A soma entre {} e {} é {}'.format(num1, num2, soma))
    #Opção de multiplicação
    if opçao == 2:
        mult = num1 * num2
        print('A multiplicação entre {} e {} é {}'.format(num1, num2, mult))
    #Opção de comparação númerica
    if opçao == 3:
        if num1 > num2:
            maior = num1
        if num1 < num2:
            maior = num2
        print('O valor maior entre {} é {} será {}'.format(num1, num2, maior))
    #Opção de troca de valores
    if opçao == 4:
        num1 = int(input('Digite o 1º valor: '))
        num2 = int(input('Digte o 2º valor: '))
    elif opçao == 5:
        print('Finalizando...')
    print('-=-' * 10)
    sleep(2)
print('                       PROGRAMA FINALIZADO!')
print('\033[32m-*-\033[m' * 22)

