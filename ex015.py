# Escreva um program que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias
# pelos quais ele foi alugado. Calcule o preço a pagar sabendo que o carro custa R$60 por dia e R$0.15 por Km rodado.

print('\n      ====== DESAFIO 15 ======      ')

d = int(input('\nQuantos dias você passou com o carro? D = '))
km = float(input('Quantos kilômetros foram rodados? Km = '))

print('\nCALCULANDO:')
print(f'Você ficou {d} dias com o carro. O custo dos dias é de R${d*60:.2f}.')
print(f'Você rodou {km:.2f}km com o carro. O custo dos Km é de R${km*0.15:.2f}.')
print(f'Ao total seu aluguel dos dias e km rodados é de R${(km*0.15)+(d*60)}.')
