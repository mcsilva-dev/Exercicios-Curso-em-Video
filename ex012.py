# Faça um algoritimo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

print('\n     ====== DESAFIO 12 ====== ')

print('\nA loja está em liquidação. Todas as compras terão desconto de 5%.')
valor = float(input('Qual valor da sua compra? R$'))
desc = valor * 5 / 100

print(f'Sua compra de R${valor} aplicando 5% de desconto, terá um desconto de R${desc:.2f}.\n'
      f'O valor final da compra após aplicado o desconto é de R${valor-desc:.2f}.\n'
      f'Agradecemos pela sua compra!')
