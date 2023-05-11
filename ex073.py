"""Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de
colocação. Depois mostre:
A) Apenas os 5 primeiros colocados.
B) Os últimos 4 colocados da Tabela.
C) Uma lista com os times em ordem alfabetica.
D) Em que posição na tabela está o time da Chapecoense."""

print("\n", "DESAFIO 74".center(60), "\n")

tabela = ('Botafogo', 'Palmeiras', 'Cruzeiro', 'Fortaleza', 'São Paulo', 'Fluminense', 'Grêmio', 'Internacional',
          'Bahia', 'Athletico-PR', 'Vasco', 'Bragantino', 'Cuiabá', 'Santos', 'Atlético-MG', 'Flamengo', 'Corinthians',
          'Goiás', 'Coritiba', 'América-MG')

print(f"{'TABELA DO BRASILEIRÃO':-^50}")

for classificacao, time in enumerate(tabela):
    print(f"{classificacao + 1:4}: {time:15}")

print('-' * 50)
print(f"\n{'PRIMEIROS 5 COLOCADOS:':-^50}")

for colocacao, time in enumerate(tabela[:5]):
    print(f"{colocacao + 1:4}: {time:15}")

print('-' * 50)
print(f"\n{'OS 4 ÚLTIMOS DA TABELA:':-^50}")

for time in tabela[16:]:
    print(f"{tabela.index(time) + 1:4}: {time:15}")

print('-' * 50)
print(f"\n{'TABELA EM ORDEM ALFABÉTICA':-^50}")

for time in sorted(tabela):
    print(f'{time:^50}')

print('-' * 50)
print(f"\n{'POSIÇÃO DA CHAPECOENSE NA TABELA':-^50}")

if 'Chapecoense' in tabela:
    print(f"A Chapecoense está na {tabela.index('Chapecoense') + 1}ª posição")
else:
    print(f"{'Chapecoense não se encontra na tabela':^50}")
