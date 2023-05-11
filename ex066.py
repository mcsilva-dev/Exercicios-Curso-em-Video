"""Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o
valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles.
(desconsiderando o flag)"""

print("\n", "DESAFIO 66".center(60), "\n")
valores = 0  # Acumula o número total de números que foram digitados pelo usuário.
soma = 0  # Soma os números que foram digitados pelo usuário.
while True:
    numero = int(input("Digite um número inteiro (0 para sair): "))  # Recebe o número que o usuário digitar.
    if numero == 0:  # Confere se o valor não é o Flag
        break  # Caso for o flag, o looping é interrompido.
    soma += numero  # Soma o número digitado pelo usuário à variavel soma.
    valores += 1  # A cada numero digitado pelo usuário acrescenta 1 no acumulador.
print(f"A soma do(s) {valores} número(s) digitado(s) é {soma}")  # Apresenta ao fim a soma e a quantidade de números
# digitados
