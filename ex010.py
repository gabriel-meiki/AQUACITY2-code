# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# OBS: U$ 1,00 = R$ 3,27 (5,46)
# EURO = 6,33
# iene = 0,048 reais
r = float(input('Quanto dinheiro você tem na carteira ? R$'))
d = r / 5.46
e = r / 6.33
i = r / 0.048
print('Com R${} você pode comprar US${:.2f}, €{:.2f} ou ¥{:.2f}'.format(r, d, e, i))
