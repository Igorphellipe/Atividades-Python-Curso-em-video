print('GERADOR DE PA')
print('-=-' * 10)
p = int(input('Digite o 1º termo: '))
r = int(input('Digite a razão: '))
termo = p
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo = termo + r
    cont = cont + 1
print('Fim')

