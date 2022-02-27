#Crie um programa que leia dois números e mostre a soma entre eles
num1 = int(input('Diga valor: '))
num2 = int(input('Diga outro valor: '))
soma = num1 + num2
print('A soma entre {} e {} é igual a {}!'.format(num1, num2, soma))
print(type(soma))