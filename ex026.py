# Faça um programa  que leia uma frase pelo teclado e mostre:
# > Quantas vezes aparece a letra "A".
# > Em que posição aparece a primera vez.
# > Em que posição ela aparece a última vez.

print(f'\n{"====== DESAFIO 26 ======":^37}')

frase = input('\nDigite uma frase: ').strip()
a = frase.upper().count('A')
pa = frase.upper().find('A')
ua = frase.upper().rfind('A')

print(f'A letra "A" aparececeu {a} vezes na frase.')
print(f'A primeira ocorrência da letra "A" ocorreu na posição {pa}.')
print(f'A ultima ocorrência da letra "A" é ocorreu posição {ua}')
