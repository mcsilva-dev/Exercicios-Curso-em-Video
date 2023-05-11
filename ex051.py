# Desenvolva um programa que leia o termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

print(f"\n{'====== DESAFIO 51 ======':^60}\n")
print(f"{'OS 10 PRIMEIROS TERMOS DE UMA PA':^60}\n")

termo = int(input('Informe o primeiro termo da PA: '))  # Primeiro termo é o valor de contagem inicial.
razao = int(input('Informe a razão da PA: '))  # A razão será o valor acrescentado para diferenciar cada termo.

print('-=-' * 10)
for contagem in range(1, 11):
    print(f"O {contagem}° termo é {termo}")  # Exibe o termo.
    termo += razao  # Acrescenta no termo o valor de sua razão.
print('-=-' * 10)
