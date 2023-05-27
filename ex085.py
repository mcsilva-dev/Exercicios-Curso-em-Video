"""Crie um programa onde o usuário possa digitar sete valores númericos e cadastre-os em uma lista única que mantenha
separado os valores pares e impares. No final mostres os valor pares e impares em ordem crescente."""

print("\n", "DESAFIO 85".center(38), "\n")

lista = [[], []]  # Cria uma lista, com dois elementos, que são listas também.

for x in range(0, 7):  # Cria um laço para registrar 7 valores.
    valor = (int(input(f"Digite o {x + 1}º valor: ")))  # Recebe o valor digitado pelo usuário.
    if valor % 2 == 0: # Se o valor for par, ele irá adicionar a lista do elemento numero 0.
        lista[0].append(valor)
    else:  # Senão, sera adicionado a lista 1.
        lista[1].append(valor)

# Por fim é apresentado ao usuário o resultado.
print("-" * 40)
print(f"Os valores pares digitados foram: {sorted(lista[0])}")
print(f"Os valores impares digitados foram: {sorted(lista[1])}")
