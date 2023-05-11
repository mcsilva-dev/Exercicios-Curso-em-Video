# Faça um programa que leia 3 números e mostre qual é o maior e qual é o menor.

print(f"\n{'====== DESAFIO 33 ======':^37}\n")

n1 = int(input('Digite o um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
n3 = int(input('Digite o último número inteiro:'))
maior = n1
menor = n1
cores = {'Vermelho': '\033[1;31m',
         'Verde': '\033[1;32m',
         'Limpa': '\033[m'}

if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print(f'O maior valor digitado é {cores["Verde"]}{maior}{cores["Limpa"]}.')
print(f'O menor valor digitado é {cores["Vermelho"]}{menor}{cores["Limpa"]}.')
