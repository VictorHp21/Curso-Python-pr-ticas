velocidade = int(input('Digite a velocidade de um carro em km/h: '))

if velocidade > 80:
    print("Multado!")
    multa = (velocidade - 80) * 7
    print(f'Valor da multa: R${multa}')
else:
    print('Dentro do limite de velocidade!')