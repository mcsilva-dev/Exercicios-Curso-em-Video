# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

print('\n     ====== DESAFIO 08 ======')

m = float(input('\nDigite uma medida em metros: '))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000

print(f'a medida de {m:.2f} corresponde a:\n'
      f'{km}km\n'
      f'{hm}hm\n'
      f'{dam}hm\n'
      f'{dm}dm\n'
      f'{cm}cm\n'
      f'{mm}mm\n')
