from math import sqrt,ceil, floor

num = int(input('Digite um número: '))

raiz = sqrt(num)

#ceil arredonda pra cima
#floor arredonda pra baixo
print('a raiz deste numero arredonda pra cima é: {}'.format(ceil(raiz)))

print('a raiz deste numero arredonda pra baixo é: {}'.format(floor(raiz)))

print('a raiz deste numero é: {}'.format(raiz))
