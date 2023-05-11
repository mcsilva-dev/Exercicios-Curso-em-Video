# Faça um programa que leia o peso de cinco pessoas. No final mostre qual foi o maior e menor peso lidos.

print(f"\n{'====== DESAFIO 55 ======':^60}\n")
print(f"{'PESANDO PESSOAS':^60}\n")

maior_peso = 0
menor_peso = 0

for contagem in range(1, 6):
    peso = float(input(f"Digite o peso da {contagem}° pessoa(Kg): "))
    if contagem == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        if maior_peso < peso:
            maior_peso = peso
        elif menor_peso > peso:
            menor_peso = peso

print('-=-' * 12)
print(f"O maior peso registrado foi {maior_peso}Kg.")
print(f"O menor peso registrado foi {menor_peso}Kg.")
print('-=-' * 12)
