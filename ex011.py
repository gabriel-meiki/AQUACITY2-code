# Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pinta-la,
# sabendo que cada litro de tinta, pinta uma área de 2m²
largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura * altura
t = area / 2
print('Sua parede tem a dimenção {}x{} e sua área é de {}m².'.format(largura, altura, area))
print('Para pintar essa parede, você precisará de {}L de tinta'.format(t))
