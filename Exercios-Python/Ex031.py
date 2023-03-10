print('\033[33;4m ****************** Calculando Passagem *********************\033[m')
km = int(input('Digite quantos KM será sua viagem: '))
dis_pq  = float(km * 0.50)
dis_gr  = float(km * 0.45)
if km <= 200:
    print('Sua viagem de {}KM ficará no valor de R$:{}'.format(km,dis_pq))
else:
    print('Sua viagem de {}KM ficará no valor de R$:{}'.format(km,dis_gr))
print('Boa viagem!')