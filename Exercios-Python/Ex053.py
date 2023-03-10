print('-=-' * 22)
print('                    \033[1;4mDESCOBRINDO UM PALÍNDROMO\033[m')
print('-=-' * 22)

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
#fatiamento de strings
#inverso = junto [::-1]
for letra in range(len(junto)-1, -1, -1):
    inverso = inverso + junto[letra]
print('O inverso de {} é {}' .format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('Está frase não é palíndromo')