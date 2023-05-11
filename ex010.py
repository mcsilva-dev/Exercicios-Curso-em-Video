# Crie um programa que leia quanto dinhero uma pessoa tem na carteira e quantos Dólares ela pode comprar
# Considere US$1,00 = R$3,27

print('\n      ====== DESAFIO 10 ======')

real = float(input('\nQuantos reais você tem ai na sua carteira? R$'))
dolar = real / 5.2754
euro = real / 5.7309

print(f'Com R${real:.2f}, você consegue comprar US${dolar:.2f}.')
print(f'Mas, se preferir, esses R${real} podem comprar EU${euro:.2f}')
