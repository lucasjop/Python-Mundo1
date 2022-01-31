'''
Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
'''

print('===== Exercício 08 =====')
n1 = int(input('Digite o valor em metros: '))
print(f'{n1}m = {100*n1}cm', end=' e ')
print(f'{n1}m = {1000*n1}mm')