"""Crie um programa que leia varios números inteiros pelo teclado. No final da execução, mostre a média entre todos os
valores e qual foi o maior e menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a
digitar valores."""

print("\n", "DESAFIO 65".center(30), "\n")

soma = 0  # Variavel para fazer a soma dos valores digitados pelo usuário.
total_numeros = 0  # Variavel responsável por acumular o total de números digitados pelo usuário.
maior = 0  # Variavel que guarda o maior valor digitado pelo usuário.
menor = 0  # Variavel que guarda o menor valor digitado pelo usuário.

while True:  # Iniciando o looping
    numero = int(input("Digite um número inteiro: "))  # Recebendo do usuário um número inteiro.
    total_numeros += 1  # Sempre que for digitado um número, o total de numeros será incrementado com +1.
    soma += numero  # Soma recebe o valor de número somado ao seu proprio valor.
    if total_numeros == 1:  # Caso não tenha sido digitado nenhum número anteriormente, ou seja, o total_numeros seja 0
        # será executado o bloco a seguir, que torna o número o maior e menor.
        maior = menor = numero  # O maior valor e menor valor recebem o valor de número.
    else:  # Se não for o primeiro número digitado, irá entrar neste bloco.
        maior = numero if numero > maior else maior  # Caso o maior valor seja menor que o numero, ele recebe o numero.
        menor = numero if numero < menor else menor  # Caso o maior valor seja menor que o numero, ele recebe o numero.
    while True:  # Looping com a finalidade de garantir com que o usuário responda corretamente.
        pergunta = input("Deseja continuar [S/N]?").upper().strip()  # Recebe a resposta e transforma em maiusculo.
        if pergunta == 'S':  # Se o usuário digitar 'S' é executado o bloco a seguir e o looping é interrompido.
            print("-=-" * 10)
            break
        elif pergunta == 'N':  # Se o usuário digitar 'N' é executado o bloco a seguir e o looping é interrompido.
            print("-=-" * 10)
            break
        else:  # Caso o usuário responda de forma incorreta, será exibido uma mensagem solicitando que digite novamente.
            print("Opção inválida. Digite novamente!")
    if pergunta == 'N':  # Se a resposta do usuário for não o looping principal também é interrompido.
        break

media = soma / total_numeros  # calcula a média dos números digitados pelo usuário.

# Após finalizado, será exibido ao usuário as estatisticas de média, maior e menor. Por fim o programa é encerrado.
print(f"Média = {media:.2f}")
print(f"Maior = {maior}")
print(f"Menor = {menor}")

