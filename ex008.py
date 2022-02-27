# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros
medida = float(input('Uma distância em metros: '))
print('\nA medida de {} m corresponde a'.format(medida))
km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print('\n{} km \n{} hm \n{} dam \n{} dm \n{} cm \n{} mm'.format(km, hm, dam, dm, cm, mm))
