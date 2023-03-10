print('\033[32m-=-\033[m' * 22)
print('                      \033[1;4mCADASTRO DE PESSOAS\033[m')
print('\033[32m-=-\033[m' * 22)
cont_p = 0
cont_m = 0
cont_f = 0
while True:
    print('--' * 22)
    print('            CADASTRE UMA PESSOA')
    print('--' * 22)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    print('==' * 22)
    # Contador de pessoas com mais 18
    if idade > 18:
        cont_p = cont_p + 1
    # Contador de quantos homens cadastrados
    if sexo in 'Mm':
        cont_m = cont_m + 1
    # Contador de Mulheres com Menos de 20 anos
    if sexo in 'Ff' and idade < 20:
        cont_f = cont_f + 1
    cond = ' '
    while cond not in 'SN':
        cond = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if cond == 'N':
        break

print('**' * 22)
print('====== FIM DO PROGRAMA ======')
print(f'Total de pessoas cadastradas mais de 18 anos: {cont_p}')
print(f'Ao todo temos {cont_m} homen(s) cadastrados!')
print(f'E temos {cont_f} mulheres com menos de 20 anos')


