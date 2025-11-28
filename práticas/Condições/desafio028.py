import random

num = random.randint(0,5)

op = int(input('Digite um número de 0 a 5: '))

while op != num:
 if op > num:
    print('Errado! tente novamente')
    print('Dica: O número sorteado é menor do que o digitado')
 else:
    print('Errado! tente novamente')
    print('Dica: O número sorteado é maior do que o digitado')

 op = int(input('Digite outro número: '))


print('Parabéns você acertou!')