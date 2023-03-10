'''print('-------- Descobrido Números Maiores e Menores ----------')
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))
maior = num1
menor = num1
verificando o maior
if (num2 > maior):
    maior = num2
if  (num3 > maior):
    maior = num3
verificando o menor
if (num2 < menor):
    menor = num2
if (num3 < menor):
    menor = num3

print('O maior número é {} e o menor é {} !'.format(maior, menor))

print('---------- FIM ----------')'''

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int = int(input('Terceiro valor: '))
#verificando o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
#Verificando quem e maior
maior = a
if c > a and c > b:
    maior = c
if b > a and b > c:
    maior = b
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))