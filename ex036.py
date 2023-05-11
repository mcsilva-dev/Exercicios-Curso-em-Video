# Escreva um programa para aprovar o empréstimo bancário para a compa de uma casa. O programa vai perguntar o
# valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal sabendo que ela não pode exceder 30% do salário ou então o empréstimo será
# negado.

# importando a ferramente sleep da biblioteca time, para causar o efeito de processamento.
from time import sleep
# adicionando um dicionário de cores.
cores = {
    'verde': '\033[1;32m',
    'vermelho': '\033[1;31m',
    'limpa': '\033[m'
}

# interagindo inicialmente com o cliente.
print(f"\n{cores ['verde']}{'====== DESAFIO 36 ======':^60}{cores['limpa']}\n")
print(f'{"SIMULAÇÃO DE EMPRÉSTIMO":^60}\n')
print('Seja bem-vindo ao Banco Silva!')
print('Vamos iniciar sua simulação para empréstimo imobiliário.')

# captando informações importantes com o usuário, sendo elas o valor do imóvel, salário e anos que prentende quitar.
imovel = float(input(f'Por favor, insira o valor do {cores["vermelho"]}IMÓVEL{cores["limpa"]}: R$'))
sleep(1)
salario = float(input(f'Insira aqui o valor de seu {cores["verde"]}SALÁRIO{cores["limpa"]}: R$'))
sleep(1)
anos = int(input(f'Agora, informe em quantos anos pretende {cores["verde"]}QUITAR{cores["limpa"]} o imóvel: '))
meses = anos * 12
sleep(0.5)

# adicionando informações que dê sensação ao usuário que suas informações estão sendo processadas.
print('\nPROCESSANDO INFORMAÇÕES, AGUARDE...\n')
sleep(3)

# após isso será verificado se o empréstimo pode ou não ser realizado ao cliente, baseado na porcentagem que a parcela
# representará de seu salário.
if imovel / meses > salario * 30 / 100:
    print(f'Sentimos muito, mas seu empréstimo foi {cores["vermelho"]}NEGADO{cores["limpa"]}!')
    print(f"O motivo é que as parcelas ultrapassaram 30% do seu salário."
          f"\nO valor de cada parcela seria {cores['verde']}"
          f"R${imovel / meses:.2f}{cores['limpa']} o que corresponde à "
          f"{cores['vermelho']}{(imovel / meses * 100 / salario):.2f}{cores['limpa']}% do seu salário.")
else:
    print(f"Pode comemorar, seu empréstimo foi {cores['verde']}APROVADO!{cores['limpa']}")
    print(f"Cada parcela ficará em {cores['verde']}R${imovel / meses:.2f}{cores['limpa']}."
          f"\nEsse valor corresponde à {cores['verde']}{(imovel / meses * 100 / salario):.2f}%{cores['limpa']}"
          f" do seu salário.")
