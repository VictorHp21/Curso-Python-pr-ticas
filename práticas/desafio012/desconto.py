precoInicial = float(input('Qual é o preço do produto? R$:'))

desconto = 0.05

precoComdesconto = (precoInicial - (precoInicial * desconto))

print(f'O produto que custava R${precoInicial}, na promoção com desconto de 5% vai custar R${precoComdesconto:.2f}')