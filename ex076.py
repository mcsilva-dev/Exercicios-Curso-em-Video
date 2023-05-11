"""Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular."""

print("\n", "DESAFIO 76".center(60), "\n")

produtos = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99,
            'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)

print('-' * 60)
print('LISTAGEM DE PREÇOS'.center(60))
print('-' * 60)

for produto in produtos:
    if produtos.index(produto) % 2 == 0:  # se o indice do produto for par é uma string, observe na tupla.
        print(f'{produto:.<50}', end="")
    else:
        print(f'R${produto:>8.2f}')

print('-' * 60)
