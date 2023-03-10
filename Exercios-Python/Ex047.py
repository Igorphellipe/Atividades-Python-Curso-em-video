print('\033[32m-=-\033[m' * 22)
print('                  \033[1;4mMOSTRANDO NUMEROS PARES 1 A 50\033[m')
print('\033[32m-=-\033[m' * 22)

for c in range(1, 50+1):
    if c % 2 == 0:
        print(c)
print('FIM')