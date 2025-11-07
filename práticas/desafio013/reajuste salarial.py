salario = float(input('Qual é o salário do funcionário? R$'))

aumento = 0.15

novoSalario = (salario + (salario * aumento))

print(f'Um funcionário que ganhava R${salario}, com 15% de aumento, passa a receber R${novoSalario:.2f}')