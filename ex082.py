"""Crie um progrma que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores impares digitados,
respectivamente.
Ao final, mostre o conteúdo das três listas geradas."""

print("\n", "Desafio".center(40), "\n")

lista_principal = list()  # Cria a lista principal.
lista_pares = list()  # Cria a lista que irá receber os valores pares da lista principal.
lista_impares = list()  # Cria a lista que irá receber os valores impares da lista principal.

while True:
    lista_principal.append(int(input("Digite um número: ")))  # Recebe e adiciona à lista um número inteiro.
    while True:  # Cria um looping para garantir a resposta correta do usuário.
        resposta = input("Quer continuar? [S/N] ").strip().upper()[0]
        if resposta in "SN":
            break
        else:  # Caso o usuário não responda corretamente é solicitado que "tente novamente".
            print("Tente novamente.", end=" ")
    if resposta == "N":  # Se a resposta for 'N' o looping principal é interrompido.
        break

for numero in lista_principal:  # Percorre todos os elementos das lista principal.
    if numero % 2 == 0:  # Se o elemento for um valor par será adicionado a lista_pares
        lista_pares.append(numero)
    else:  # Caso contrário será adicionado a lista_impares.
        lista_impares.append(numero)

# Por fim é exibido os resultados finais ao usuário.
print("-" * 40)
print(f"A lista completa é {lista_principal}")
print(f"A lista de pares é {lista_pares}")
print(f"A lista de ímpares é {lista_impares}")
