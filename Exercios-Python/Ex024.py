print('-----$$$ Verificando cidades $$$-----')
cidade = str(input('Digite o nome da sua cidade: ')).strip()
cid = (cidade[:5].upper() == 'SANTO')
print('A sua cidade contem o nome Santo?  {}'.format(cid))
