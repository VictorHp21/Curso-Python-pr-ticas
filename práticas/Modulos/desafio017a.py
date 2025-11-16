from math import sqrt
catOposto = float(input('digite o cateto oposto: '))

catAdja = float(input('digite o cateto adjacente: '))

hipotenusa = sqrt(catOposto**2 + catAdja**2)

print(f'O valor da hipotenusa é: {hipotenusa}')
