"""Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão
usando a estrutura while"""

print("\n", "DESAFIO 61".center(30), "\n")
print("EXECUTANDO UMA PA". center(30), "\n")

termo = int(input(f"{'Primeiro Termo'.upper()} da PA: "))  # Recebe do usuário o primeiro termo da PA.
razao = int(input(f"{'Razão'.upper()} da PA: "))  # Recebe do usuário a razão da PA.
contagem = 0  # Variavel utilizada como contador.

print("-=-" * 19)

while contagem < 10:  # Enquanto o contador for menor que 10, este bloco será executado.
    print(f"{termo} -> " if contagem < 9 else f"{termo}\n", end="")  # Apresenta o termo da PA e sua posição.
    termo += razao  # Acrescenta ao termo a razão da PA.
    contagem += 1  # Adiciona 1 ao contador.

print("-=-" * 19)
