print("\n", "FATORIAL".center(60), "\n")
numero = int(input("Digite um número para exibir seu fatorial: "))
total = 1
print(f"{numero}! = ", end="")
for contagem in range(numero, 0, -1):
    total *= contagem
    print(f"{contagem} * " if contagem > 1 else f"{contagem} = ", end="")
print(total)
