algo = input('Diga qualquer coisa: ')
print('O tipo primitivo do valor {} é'.format(algo), type(algo))
print('O valor *{}* só tem espaços? '.format(algo), algo.isspace())
print('O valor *{}* tem somente números? '.format(algo), algo.isnumeric())
print('O valor *{}* tem somente letras? '.format(algo), algo.isalpha())
print('O valor *{}* é alfanumérico? '.format(algo), algo.isalnum())
print('O valor *{}* é todo maiúsculo? '.format(algo), algo.isupper())
print('O valor *{}* é todo minúsculo? '.format(algo), algo.islower())
print('O valor *{}* é capitalizado? '.format(algo), algo.istitle()) #junção de letra maiúscula e minúscula
