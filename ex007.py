# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

print('\n      ====== DESAFIO 07 ======      ')

n1 = float(input('\nDigite sua primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2

print(f'A média entre {n1:.1f} e {n2:.1f} é igual a {m:.1f}.')

# Professor não solicitou, mas tive a vontade de implementar estas linhas ao codigo.
print('\nRESULTADO:')
if m < 7:
    print('Lamento! Você não foi aprovado(a).')
else:
    print('Parabéns! Você foi aprovado(a)!')
