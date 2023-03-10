print('\033[32m-*-\033[m' * 22)
print('                   \033[1;4mCOMPARANDO STRINGS COM WHILE\033[m')
print('\033[32m-*-\033[m' * 22)

sexo = str(input('Digte [M/F]: ')).upper()[0].strip()
while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos, por favor tente novamento [M/F]: ')).upper()[0].strip()
print('O {} está correto!'.format(sexo))