# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

print(f'\n{"====== DESAFIO 26 ======":^37}')

while True:
    nome = input('\nDigite seu nome: ').strip()
    if len(nome) > 2:
        # Verifica se dentro todos os caracteres do nome, se existe algum que não seja alfabetico.
        if ''.join(nome.replace(' ', '').lower()).isalpha():
            print(f'\n{"Analisando Nome":-^37}')
            if 'SILVA' in nome.upper():
                print('Seu nome contém "SILVA".')
            else:
                print('Seu nome não contém "SILVA"')
            break
        else:
            print('<<<O nome deve conter apenas letras>>>')
    else:
        print(f'<<<O nome deve conter no minímo 3 caracteres>>>')
