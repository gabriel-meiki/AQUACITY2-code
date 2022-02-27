# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
cels = float(input('Informe a temperatura em °C: '))
fahr = 9 * cels / 5 + 32
print('A temperatura de {}°C corresponde a {}°F!'.format(cels, fahr))
