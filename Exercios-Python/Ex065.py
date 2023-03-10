print('\033[32m-=-\033[m' * 22)
print('                    \033[1;4m CALCULANDO VALORES\033[m')
print('\033[32m-=-\033[m' * 22)
resp = 'S'
soma = 0
quant = 0
media = 0
maior = 0
menor = 0
while resp in 'Ss':
    num = int(input('Digite um valor: '))
    soma = soma + num
    quant = quant + 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    resp = str(input('Quer continuar [S/N]: ')).strip().upper()
media = soma / quant
print('Você digitou {} números e a média foi {}'.format(quant, media))
print('O maior Número entre eles é {} e o menor é {}'.format(maior, menor))
print('FIM')