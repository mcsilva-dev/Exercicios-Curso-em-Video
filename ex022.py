# Crie um programa que leia o nome completo de uma pessoa e mostre:
# > O nome com todas as letras maiúsculas.
# > O nome com todas minúsculas.
# > Quantas letras ao todo (sem considerar espaços)
# > Quantas letras tem o primero nome.

print('\n      ====== DESAFIO 22 ======      ')

# Recebendo informação do usuário sobre seu nome e já anulando espaços possíveis no começo e no fim.
nome = input('\nDigite seu nome completo: ').strip()

# Dividindo o nome do usuário em uma lista.
divido = nome.split()

# Após dividir, junto o nome novamente, porém não deixando espaços entre as palavras da lista, deixando assim
# mais fácil para que eu consiga informar exatamente quantas letras o nome dele possui.
sespace = ''.join(divido)

print(f'\n{"ANALISANDO SEU NOME":-^40}')
print(f'Seu nome com letras maiúsculas: {nome.upper()}.')
print(f'Seu nome com letras minúsculas: {nome.lower()}.')
print(f'Ao todo seu nome tem {len(sespace)} letras.')
print(f"seu primeiro nome '{divido[0]}' possui {len(divido[0])} letras.")

