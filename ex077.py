"""Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar,
para cada palavra, quais são as suas vogais."""

print("\n", "DESAFIO 77".center(60), "\n")

palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar',
            'mercado', 'programador', 'futuro')

for palavra in palavras:
    print(f"Na palavra {palavra.upper()} temos", end=' ')
    for letra in palavra:
        if letra in 'aeiou':
            print(letra, end=' ')
    print()
