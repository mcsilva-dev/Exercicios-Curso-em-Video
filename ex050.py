# Desenvolva um programa que leia seis número inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.

print(f"\n{'====== DESAFIO 50 ======':^60}\n")
soma = 0
par = 0
for contagem in range(1, 7):
    numero = int(input(f"Digite o {contagem}° valor: "))
    if numero % 2 == 0:
        soma += numero
        par += 1
print("=" * 48)
print(f"Você digitou {par} números PARES.")
print(f"A soma dos números PARES digitados é igual a {soma}.")
print("=" * 48)
