# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - EQUILATERO: todos os lados iguais.
# - ISÓSCELES: dois lados iguais.
# - ESCALENO: todos os lados diferentes.

cores = {
    'vermelho': '\033[1;31m',
    'verde': '\033[1;32m',
    'azul': '\033[1;34m',
    'limpa': '\033[m'
}

print(f"\n{'====== DESAFIO 42 ======':^60}\n")
print(f"{'FORMANDO TRIÂNGULOS':^60}\n")

l1 = int(input('Informe o comprimento da 1° reta: '))
l2 = int(input('Informe o comprimento da 2° reta: '))
l3 = int(input('Informe o comprimento da 3° reta: '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print(f"As retas informadas {cores['verde']}PODEM FORMAR{cores['limpa']} um triângulo.")
    if l1 != l2 == l3 or l1 == l2 != l3 or l1 == l3 != l2:
        print(f"O triângulo formado é {cores['azul']}ISÓSCELES{cores['limpa']}.")
    elif l1 == l2 == l3:
        print(f"O triângulo formado é {cores['azul']}EQUILÁTERO{cores['limpa']}.")
    else:
        print(f"O triângulo formado é {cores['azul']}ESCALENO{cores['limpa']}.")
else:
    print(f"As retas informadas {cores['vermelho']}NÃO FORMAM{cores['limpa']} um triângulo.")
