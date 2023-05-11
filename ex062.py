"""Melhore o DESAFIO 061, perguntando ao usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele
disser que quer mostrar 0 termos."""

print("\n", "DESAFIO 062".center(30), "\n")
print("PROGRESSÃO ARITIMÉTICA 3.0".center(30), "\n")

termo = int(input("Primero termo da PA: "))  # Recebe do usuário o termo da PA.
razao = int(input("Razão da PA: "))  # Recebe do usuário a razão da PA.
contador = 1  # Variavel utilizada para contagem.
inicio = 10  # Valor inicial para exibir os 10 termos.
total = 0  # Acumulador de quantos termos foram exibidos.

print("-=-" * 16)

while inicio != 0:  # Enquanto o valor do contador for menor ou igual a 10. será executado todo o bloco a seguir.
    total += inicio
    while contador <= total:
        print(f"{termo} -> " if contador < total else f"{termo} -> PAUSA\n", end="")
        termo += razao  # O termo será somada a razão.
        contador += 1  # Sempre ao fim do laço será acrescentado um no valor do contador.
    inicio = int(input("Deseja exibir mais quantos termo (0 = encerrar)? "))  # Recebe do usuário a quantidade
    # de termos a mais o mesmo deseja exibir, caso digite 0 será encerrado o programa.

print("-=-" * 16)
print(f"Progressão finalizada com {total} termos exibidos.")
