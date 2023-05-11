# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário
# 2 para octal
# 3 para hexadecimal

cores = {
    'vermelho': '\033[1;31m',
    'verde': '\033[1;32m',
    'limpa': '\033[m'
}
print(f"\n{cores['verde']}{'====== DESAFIO 37 ======':^60}{cores['limpa']}\n")

c = 0
numero = int(input('Digite um número: '))
escolha = int(input('Você quer ver este numero em:'
                    '\n1 - Binário'
                    '\n2 - Octal'
                    '\n3 - Hexadecimal'
                    '\nSua opção: '))

if escolha == 1:
    print(bin(numero))
elif escolha == 2:
    print(oct(numero))
elif escolha == 3:
    print(hex(numero))


