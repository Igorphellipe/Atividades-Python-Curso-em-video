print('!!!! Controle de aumento salarial !!!! \n')
nome = input('Digite o nome do funcionario: ')
setor = input('Digite a função: ')
salario = float(input('Digite o salario do Funcionario: '))
aumento = salario+(salario*0.15)
print('O Funcionário {}, no BGP {} recebe o valor de R${:.2f} '.format(nome,setor,salario))
print('Com os cursos cadastrados o Funcionario {} terá que 15% de aumento no salario. De R${:.2f} para R${:.2f} salario total'.format(nome,salario,aumento))