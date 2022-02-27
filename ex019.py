# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que leia o nome deles e escrevendo o nome do escolhido.

import random
# from random import choice

aluno1 = str(input('Primeiro aluno(a): '))
aluno2 = str(input('Segundo aluno(a): '))
aluno3 = str(input('Terceiro aluno(a): '))
aluno4 = str(input('Quarto aluno(a): '))

lista = [aluno1, aluno2, aluno3, aluno4]

escolhido = random.choice(lista)
# escolhido = choice(lista)

print('O aluno(a) escolhido(a) foi {}'. format(escolhido))
