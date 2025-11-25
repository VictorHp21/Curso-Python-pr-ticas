from tokenize import String

nome = (input('Digite seu nome: '))

print(f'Seu nome todo em maiscúlo é: {nome.upper()}')

print(f'Seu nome todo em minúsculo é: {nome.lower()}')

print(f'Letras ao todo sem considerar espaços {len(nome.replace(" ", ""))}')

print(f'Seu primeiro nome tem: {len(nome.split()[0])} letras')
