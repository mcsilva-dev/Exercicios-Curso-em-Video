# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# > A média de idade do grupo.
# > Qual é o nome do homem mais velho.
# > Quantas mulheres têm menos de 20 anos.

print(f"\n{'====== DESAFIO 56 ======':^60}\n")

soma_idade = 0
mulher_menos20 = 0
homem_velho = ''
idade_velho = 0

for contagem in range(1, 5):
    print(f"{f'----- {contagem}ª PESSOA -----'}")
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').upper().strip()
    soma_idade += idade
    if sexo == 'M':
        if idade_velho == 0:
            homem_velho = nome
            idade_velho = idade
        else:
            if idade_velho < idade:
                homem_velho = nome
    elif sexo == 'F':
        if idade < 20:
            mulher_menos20 += 1
print('-=-' * 10)

media = soma_idade / 4

print(f"A média de idade do grupo é {media:.1f} anos.")
print(f"O homem mais velho é o {homem_velho}, ele tem {idade_velho} anos.")
print(f"{mulher_menos20} mulheres tem menos de 20 anos.") if mulher_menos20 >= 2 \
    else print(f"Apenas uma mulher tem menos de 20 anos.")
