print('----- Separando Nomes -----')
nome = str(input('Digite seu nome completo: ')).strip().title()
n = nome.split()

print('Olá, praze te conhecer!')
print('Seu primeiro nome é: {}'.format(n[0]))
print('Seu ultimo nome é: {}'.format(n[len(n)-1]))
