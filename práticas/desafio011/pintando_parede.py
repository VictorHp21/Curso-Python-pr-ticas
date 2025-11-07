Lparede = float(input('Digite a largura da parede: '))
Aparede = float(input('a altura da parede: '))

area_parede = Lparede * Aparede

#cada litro pinta uma área de 2m quadrados.

tintaNes = area_parede / 2

print(f'Sua parede tem a dimensão de {Lparede}x{Aparede} e sua área é de {area_parede}m².\nPara pintar essa parede, você precisará de {tintaNes}L de tinta.')