from time import sleep
print('\033[32m-*-\033[m' * 20)
print('                   \033[1;4mIDENTIFICANDO TRIÂNGULOS\033[m')
print('\033[32m-*-\033[m' * 20)
print()

a = int(input('Digite um 1º segmento: '))
b = int(input('Digite um 2º segmento: '))
c = int(input('Digite um 3º segmento: '))

print('\033[32m-+-\033[m' * 20)
print('                   ANALISANDO SEGMENTOS')
print('\033[32m-+-\033[m' * 20)
sleep(3)

if a < b + c and b < a + c and c < a + b:
    print('Dados os segmentos A, B e C eles formam um Triangulo', end=' ')
    if a == b == c:
        print('EQUILATERO!')
    elif a != b != c != a:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('não formam triangulo')