print('\033[32;4m--------Calculando Aumento salarial ---------\033[m')
salario = float(input('Digite o valor do Salário no funcinario: '))
if salario >= 1250:
    aumento_10 = salario + (salario * 0.10)
    print('Seu salário receberá um reajuste de 10% ficando no valor de R$:{:.2f}'.format(aumento_10))
if salario < 1250:
    aumento_15 = salario + (salario * 0.15)
    print('Seu salário receberá um reajuste de 15% ficando no valor de R$:{:.2f}'.format(aumento_15))
print('-------FIM-------')