print('-=-' * 22)
print('           \033[1;4mDESCOBRINDO MAIOR E MENOR PESO\033[m')
print('-=-' * 22)
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Peso da {}º pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('A pessoa com maior peso tem {:.1f} KG'.format(maior))
print('A pessoa com menor peso tem {:.1f} KG'.format(menor))