print('\033[32m-=-\033[m' * 22)
print('                         \033[1;4mTABUADA 3.0\033[m')
print('\033[32m-=-\033[m' * 22)
mult = 1
c = 0
n = 0
while True:
    n = int(input('Quer ver a tabuada de qual valor: '))
    if n < 0:
        break
    print('==' * 15)
    for c in range(1, 11):
        mult = c * n
        print(f'{n} x {c} = {mult}')
    print('==' * 15)
print('==' * 15)
print('PROGRAMA ENCERRADO VOLTE SEMPRE !')

