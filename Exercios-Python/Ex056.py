print('\033[32m-=-\033[m' * 22)
print('                        \033[1;4mANALISANDO DADOS\033[m')
print('\033[32m-=-\033[m' * 22)
tot_id = 0
qnt_M = 0
homem_id = 0
nome_velho = ''
for c in range(1, 5):
    print('===== {}ª Pessoa ====='.format(c))
    nome = str(input('Nome: ')).strip().title()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo F/M: ')).strip().upper()
  # Media de idade
    tot_id = (tot_id + idade)
    media_id = tot_id / 4
    # Mulheres abaixo de 20 anos
    if sexo in 'Ff' and idade <= 20:
        qnt_M = qnt_M + 1
    # Comparando idade dos Homens
    if sexo in 'Mm' and c == 1:
        homem_id = idade
    else:
        if homem_id <= idade and sexo in 'Mm':
            homem_id = idade
            nome_velho = nome


print('A idade media do grupo é {:.1f}'.format(media_id))
print('No grupo o homem mais velho é {} e sua idade é {} ano(s)'.format(nome_velho, homem_id))
print('Temo(s) {}, com idade abaixo dos 20 anos.'.format(qnt_M))
