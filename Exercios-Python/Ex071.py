print('\033[32m-=-\033[m' * 22)
print('               ==== \033[1;4mBEM VINDO AO BANCO CRUZEIRO\033[m ====')
print('\033[32m-=-\033[m' * 22)
resto_50 = resto_20 = resto_10 = resto_1 = 0
while True:
    saque = int(input('Que valor você quer sacar? R$'))

    #Saque acima de R$50,00
    if saque >= 50:
        ced_50 = saque // 50
        resto_50 = saque % 50
        if ced_50 > 0:
            print(f'Total de {ced_50} cedulas de R$50')
        if resto_50 != 0:
            ced_20 = resto_50 // 20
            resto_20 = resto_50 % 20
            if ced_20 > 0:
                print(f'Total de {ced_20} cedulas de R$20')
            if resto_20 == 0:
                break
        if resto_20 != 0:
            ced_10 = resto_20 // 10
            resto_10 = resto_20 % 10
            if ced_10 > 0:
                print(f'Total de {ced_10} cedulas de R$10')
            if resto_10 == 0:
                break
        if resto_10 != 0:
            ced_1 = resto_10 // 1
            resto_1 = resto_10 % 1
            if ced_1 > 0:
                print(f'Total de {ced_1} cedulas de R$1')
            if resto_1 == 0:
                break
        if resto_50 == 0:
            break
    #Saque de valores acima de R$20,00
    if saque >= 20:
        ced_20 = saque // 20
        resto_20 = saque % 20
        if ced_20 > 0:
            print(f'Total de {ced_20} Cedulas de R$20')
        if resto_20 != 0:
            ced_10 = resto_20 // 10
            resto_10 = resto_20 % 10
            if ced_10 > 0:
                print(f'Total de {ced_10} cedulas de R$10')
            if resto_10 == 0:
                break
        if resto_10 != 0:
            ced_1 = resto_10 // 1
            resto_1 = resto_10 // 1
            if ced_1 > 0:
                print(f'Total de {ced_1} cedulas de R$1')
            if resto_1 == 0:
                break
        if resto_20 == 0:
            break

    #saque Valores acima de R$10
    if saque <= 20:
        ced_10 = saque // 10
        resto_10 = saque % 10
        if ced_10 > 0:
            print(f'Total de {ced_10} cedulas de R$10')
        if resto_10 == 0:
            break
        if resto_10 != 0:
            ced_1 = resto_10 // 1
            resto_1 = resto_10 // 1
            if ced_1 > 0:
             print(f'Total de {ced_1} cedulas de R$1')
            if resto_1 == 0:
                break
    break

print('==' * 22)
print('\033[1mO BANCO CRUZEIRO AGRADECE A PREFERÊNCIA! TENHA UM BOM DIA!\033')