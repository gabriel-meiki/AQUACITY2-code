# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
# valor * 5 / 100 (valor * 5% ... 5% = 5/100)
# multiplica por 5 e divide por 100 (calular o valor da porcentagem)
v = float(input('Qual o preço do produto ? R$'))
nv = v - (v * 0.05)  # v - (v * 5 / 100)
print('O produto que custuva R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(v, nv))
