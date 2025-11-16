import math

angulo = float(input('digite o angulo: '))

rad = math.radians(angulo)

# Calcular seno, cosseno e tangente
seno = math.sin(rad)
cosseno = math.cos(rad)
tangente = math.tan(rad)

print(f"Seno de {angulo}° = {seno:.4f}")
print(f"Cosseno de {angulo}° = {cosseno:.4f}")
print(f"Tangente de {angulo}° = {tangente:.4f}")