# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

print(f'\n{"====== DESAFIO 24 ======":^37}')

cidade = input('Digite o nome da sua cidade: ').upper().strip()
separado = cidade.split()

print(f"Começa com a palavra 'SANTO' = {separado[0] == 'SANTO'}")
