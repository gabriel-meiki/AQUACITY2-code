# Faça um problema que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math
# CASO QUISESSE SIMPLIFICAR MAIS AINDA O CÓDIGO
# from math import radians, sin, cos, tan

angulo = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(angulo))
# seno = sin(radians(angulo))
cosseno = math.cos(math.radians(angulo))
# cosseno = cos(radians(angulo))
tangente = math.tan(math.radians(angulo))
# tangente = tan(radians(angulo))

print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
print('O angulo de {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(angulo, tangente))

# para converter os graus em radianos, usa-se "math.radians(x)".

# Pode usar um parâmetro dentro de um outro parâmetro, como por exemplo o seno, cosseno e tangente.

# Para o número não ter muitas casas decimais após a vírgula, usa-se {:.2f}