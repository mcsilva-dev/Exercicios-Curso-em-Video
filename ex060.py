"""Faça um programa que leia um número qualquer e mostre o seu fatorial.
ex: 5! = 5*4*3*2*1 = 120"""

print("\n", "DESAFIO 60".center(30), "\n")

numero = int(input("Digite um número"
                   "\npara calcular seu fatorial: "))  # Recebe o número que o usuário deseja exibir seu fatorial.
contador = numero  # cria um contador utilizando o valor da variavel numero e diminuindo 1.
total = 1  # cria um acumulador, para que seja armazenado o total do fatorial. começa com elemento neutro 1.

print(f"{numero}! = ", end="")

while contador > 0:  # Enquanto o contador for maior ou igual a 0, este bloco será executado.
    total *= contador  # Multiplica o valor do contador pelo total.
    print(f"{contador} x " if contador > 1 else f"{contador} = ", end='')  # caso o contador seja maior que 1 irá exibir
    # o valor de contador e o sinal de 'x', caso contrário será exibido o valor de contador e o sinal '='.
    contador -= 1

print(total)  # Exibe o valor que foi acumulado na variavel total após encerrar o looping.
