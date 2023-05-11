#Crie um algoritimo que leia um número e mostre o seu dobro, triplo e raiz quadrada

print('\n', ' '*6, '='*6, 'DESAFIO 06', '='*6)

n = int(input('\nDigite um número: '))
print(f"O dobro de {n} é igual a {n * 2}.\n"
      f"O triplo de {n} é igual a {n * 3}.\n"
      f"A raiz quadrada de {n} é igual a {pow(n, 1 / 2):.2f}.")
