# Crie um programa que leia uma frase e diga se ela é um palíndromo, desconsiderando os espaços.
# Ex: apos a sopa

print(f"\n{'====== DESAFIO 53 ======':^60}\n")

soma = 0
frase = input('Digite uma frase: ').strip()
frase_sem_espacos = frase.replace(' ', '').lower()  # Poderia usar tambem o split, depois join para juntar tudo.
frase_invertida = frase_sem_espacos[::-1]  # Poderia fazer também desta forma,
# percorrendo a frase ao contrário: frase_sem_espacos[::-1]

# for letra in range(len(frase_sem_espacos) - 1, -1, -1):  # forma de fazer do guanabara
#    frase_invertida += frase_sem_espacos[letra]

print(f'O inverso de "{frase_sem_espacos}" é "{frase_invertida}"')

if frase_sem_espacos == frase_invertida:
    print(f'"{frase.upper()}" é um palíndromo.')
else:
    print(f'"{frase.upper()}" não é um palíndromo.')
