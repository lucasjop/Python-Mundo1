'''
Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
'''

print('===== Exercício 04 =====')
txt = input('Digite algo: ')
print('O termo digitado é do tipo {}'.format(type(txt)))
print(f'É possível converter para número? {txt.isnumeric()}')
print(f'É possível converter para alfabeto? {txt.isalpha()}')
print(f'É possível converter para alfanumérico? {txt.isalnum()}')
print(f'Está todo em minúsculo? {txt.islower()}')
print(f'Está todo em maiúsculo? {txt.isupper()}')
print(f'Está capitalizado? {txt.istitle()}')
print(f'Só tem espaços? {txt.isspace()}')