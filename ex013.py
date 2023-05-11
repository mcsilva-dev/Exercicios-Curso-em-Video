# Faça um algoritimo que leia o sálario de um funcionário e mostre seu novo salário, com 15% de aumento.

print('\n      ====== DESAFIO 13 ====== ')

print('\nOlá, você ganhou 15% de aumento em seu salário.')
sal = float(input('Digite o valor atual do seu salario: R$'))
aum = sal * 15 / 100

print(f'Seu salário antes do aumento era R${sal:.2f},'
      f'\ncom 15% de aumento você receberá R${aum:.2f} à mais.'
      f'\nSendo assim seu novo salário é R${sal+aum:.2f}.')

