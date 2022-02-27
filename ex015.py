# Escreva um programa
# Que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

# Perguntar quantos dias e quantos quilômetros foram percorridos
dias = int(input('Quantos dias alugado ? '))
km = float(input('Quantos km rodados ? '))

# conta geral (dias + km)
pago = (dias * 60) + (km * 0.15)

# imprimir a conta
print('O total a pagar é de R${:.2f}'.format(pago))

# Dividir para conquistar (dica do prof Guanabara)

