"""Aprimore o desafio anterior, mostrando no final:
A) A soma de todos valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha."""

print("\n", "DESAFIO 87".center(43), "\n")

matriz = [[], [], []]
soma_terceira = maior_da_segunda = soma_pares = 0

for linha in range(0, 3):  # Gerando a matriz 3x3
    for coluna in range(0, 3):
        numero = int(input(f"Digite um valor para [{linha}, {coluna}]: "))  # Adicionando valor a cada posição.
        if coluna == 2:  # Verifica se esta na terceira coluna, caso estiver é somado o valor ao acumulador.
            soma_terceira += numero
        if linha == 1:  # Verifica o maior valor da linha 1
            maior_da_segunda = numero if numero > maior_da_segunda else maior_da_segunda
        if numero % 2 == 0:  # Verifica se o número é par e soma ao acumulador 'soma_pares'
            soma_pares += numero
        matriz[linha].append(numero)

print('-' * 45)

for linha in range(0, 3):  # Exibe a Matriz apos preenchida.
    for coluna in range(0, 3):
        print(f"[   {matriz[linha][coluna]}   ]", end=" " if coluna < 2 else "\n")

# Exibe as informações e dados ao usuário no final.
print('-' * 45)
print(f"A soma dos valores pares é {soma_pares}.")
print(f"A soma dos valores da terceira coluna é {soma_terceira}.")
print(f"O maior valor da segunda linha é {maior_da_segunda}.")
