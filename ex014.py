# Faça um algoritimo que converta a temperatura em graus Celsius para Fahrenheint

print('\n      ====== DESAFIO 14 ======      ')

c = float(input('\nInforme a temperatura em °C: '))
f = c * 9 / 5 + 32
k = c + 273.15

print(f'A temperatura de {c:.1f}°C corresponde à {f:.1f}°F')
print(f'E em Kelvin, corresponde à {k:.2f}K')
