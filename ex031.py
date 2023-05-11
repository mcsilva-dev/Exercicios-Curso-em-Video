# Desenvolva um programa que pergunte a distância de um viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

# Apresentação inicial ao usuário
print(f"\n{'====== DESAFIO 31 ======':^37}\n")

# Interação inicial com o usuário.
print('Olá, seja bem-vindo!')

# Recebendo a entrada do usuário informando a distância de sua viagem em Km's.
distancia = float(input('Qual distancia irá percorrer em sua viagem? '))
cores = {
    'vermelho': '\033[1;31m',
    'verde': '\033[1;32m',
    'limpa': '\033[m'
}

# Verificando e calculando o valor da passagem de acordo com a Kilometragem.
if distancia > 200:
    print(f'O valor da {cores["verde"]}passagem{cores["limpa"]} será R${distancia * 0.45:.2f}.')
else:
    print(f'O valor da {cores["vermelho"]}passagem{cores["limpa"]} será R${distancia * 0.5:.2f}.')
