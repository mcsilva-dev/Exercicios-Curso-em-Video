# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
# e todas informações possíveis sobre ele.

print('     ====== DESAFIO 04 ======      ')
t = input('Digite algo: ')
print('\nTipo primitivo desse valor é {}'.format(type(t)))
print('É um número? {}'.format(t.isnumeric()))
print('É um número decimal? {}'.format(t.isdecimal()))
print('É alfabetico? {}'.format(t.isalpha()))
print('É alfanumerico? {}'.format(t.isalnum()))
print('Só tem espaço? {}'.format(t.isspace()))
print('Tudo maiusculo? {}'.format(t.isupper()))
print('Tudo minusculo? {}'.format(t.islower()))
print('Está capitalizada? {}'.format(t.istitle()))
print('Possui digitos? {}'.format(t.isdigit()))
