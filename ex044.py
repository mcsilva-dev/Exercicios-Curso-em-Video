# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# - À vista dinheiro/pix: 10% de desconto.
# - À vista no cartão: 5% de desconto.
# - Em até 2x no cartão: preço normal.
# - 3x ou mais no cartão: 20% de juros.

print(f"\n{'====== DESAFIO 44 ======':^60}\n")
print(f"{'COMPRAS':^60}\n")
print(f"Seja bem-vindo, ao caixa! Irei lhe informar as condições de pagamento:"
      f"\n1. Dinheiro ou pix: Ganhe 10% de desconto."
      f"\n2. À vista no cartão: Ganhe 5% de desconto."
      f"\n3. Em 2x no cartão: Valor normal."
      f"\n4. 3x ou mais no cartão: 20% de acréscimo ao valor total.\n")

valor = float(input('Informe o valor da sua compra: R$'))
forma = int(input('Selecione uma das formas de pagamento informadas acima: '))

if forma == 1:
    print("Você escolheu pagar à vista no dinheiro/pix.")
    valor = valor - valor * 10 / 100
    print(f"O total a pagar pela compra é R${valor}.")
elif forma == 2:
    print("Você escolheu pagar à vista no cartão.")
    valor = valor - valor * 5 / 100
    print(f"O total a pagar pela compra é R${valor}.")
elif forma == 3:
    print("Você escolheu pagar em até 2x no cartão")
    print(f"O total a pagar pela compra é R${valor}.")
else:
    print("Você escolheu pagar em 3x ou mais no cartão.")
    parcelas = int(input('Digite o número de parcelas que deseja dividir: '))
    valor = valor + valor * 20 / 100
    print(f"O total a pagar é R${valor}, você optou por dividir em {parcelas}x.")
    parcelas = valor / parcelas
    print(f"Sendo assim, cada parcela custára R${parcelas}.")
