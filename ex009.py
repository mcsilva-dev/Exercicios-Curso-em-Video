#Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

print('      ====== DESAFIO 09 ======')

n = int(input('\nDigite um número para ver sua tabuada: '))
c = 1

print('-' * 15)
while c <= 10:
    print(f'{n} x {c:2} = {n*c}')
    c += 1
print('-' * 15)
