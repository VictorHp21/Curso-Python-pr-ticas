dias = int(input("Quantos dias alugados? "))
kmsRodados = float(input("Quantos Km rodados? "))

valorPorDia = 60
valorPorKm = 0.15

total = dias * valorPorDia + kmsRodados * valorPorKm

print(f'O total a pagar é de R${total:.2f}')