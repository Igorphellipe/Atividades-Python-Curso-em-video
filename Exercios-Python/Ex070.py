from time import sleep
print('\033[32m-=-\033[m' * 22)
print('                \033[1;4m====== SUPERMERCADO DA FAMILIA ======\033[m')
print('\033[32m-=-\033[m' * 22)
total = 0
cont = 0
cont_m = 0
produto_b = ' '
valor_m = 0
print('             ========== \033[1;4mCAIXA LIVRE\033[m ==========')
while True:

    produto = str(input('Nome do produto: ')).strip().upper()
    valor = float(input('Preço: R$ '))
    total = total + valor
    cont_m = cont_m + 1

    # Contador de produtos acima de R$1000,00
    if valor > 1000:
        cont = cont + 1
    #Comparando valores

    if cont_m == 1:
        valor_m = valor
        produto_b = produto
    else:
        if valor < valor_m:
            valor_m = valor
            produto_b = produto
    # Condição para continuar ou parar
    cond = ' '
    while cond not in 'SN':
        print('--' * 22)
        cond = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        print('--' * 22)
    if cond == 'N':
        break
print('\033[1mGERANDO CUPOM FISCAL\033[m')
print('==' * 22)
sleep(3)
print(f'O total dos produtos fica R${total:.2f}')
print(f'Tem {cont} produto(s) acima de R$1000,00')
print(f'O produto de menor valor é {produto_b} custando R${valor_m:.2f}')
print('FIM')