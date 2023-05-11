# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais o aumento é de 15%.

print(f"\n{'====== DESAFIO 34 ======':^37}\n")

cores = {'verde': '\033[1;32m',
         'limpa': '\033[m',
         'vermelho': '\033[1;31m'}
salario = float(input('Digite seu salário: R$'))

if salario > 1250:
    aumento = 10
    novo_salario = salario + (salario * aumento / 100)
else:
    aumento = 15
    novo_salario = salario + (salario * aumento / 100)

print(f'Após o aumento de {aumento}% você irá receber {cores ["vermelho"]}R${novo_salario:.2f}{cores ["limpa"]}.')
