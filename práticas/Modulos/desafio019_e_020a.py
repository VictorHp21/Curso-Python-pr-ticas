import random

nomesAlunos = ["Jeferson", "Henrique", "Victor", "Ester"]

alunoEscolhido = random.choice(nomesAlunos)

print("O aluno escolhido foi:", alunoEscolhido)

ordemDeapresentacao = random.shuffle(nomesAlunos)



print('A ordem de apresentação dos alunos é: ')
for i, nome in enumerate(nomesAlunos, start=1):
    print(f'{i}º - {nome}')