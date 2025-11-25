frase = input('Digite uma frase: ')

print(f'A letra A apareceu: {frase.lower().count('a')}')

print(f'com a letra aparecendo pela primeira vez na posição: {frase.lower().find('a')}')

print(f'E aparecendo pela ultima vez na posição: {frase.lower().rfind('a')}')