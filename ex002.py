#Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.
nome = input('Digite seu nome: ')
print('É um prazer te conhecer,', nome) #formato 1
print(f'É um prazer te conhecer, {nome}') #formato 2
print('É um prazer te conhecer, {}'.format(nome)) #formato 3, mais recomendado pela aula
#os três funcionam da mesma maneira




