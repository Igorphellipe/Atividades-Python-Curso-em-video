print('!!! Calculando o uso de tinta !!!')
largura = float(input('Qual a largura da sua parede? '))
altura = float(input('Qual a altura da sua parede? '))
area = largura*altura
tinta = area/2
print('Sua parede tem a dimensão de {}x{}, e um total de {}m².'.format(largura,altura,area))
print('Para pintar uma Area de {:.2f}M², será necessário {:.2f}Lts de tinta! '.format(area, tinta))
