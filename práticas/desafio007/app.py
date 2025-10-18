nNotas = int(input('Digite quantas notas deseja usar para calcular a media: '))

notas = []

for i in range (nNotas):
    nota = float(input(f'Digite a nota {i+1}: '))
    notas.append(nota)



media = sum(notas) / nNotas

print(f'A media das notas é: {media}')


