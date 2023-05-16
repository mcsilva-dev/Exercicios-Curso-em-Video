"""Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se
a expressão passada está com parênteses abertos e fechados na ordem correta."""

print("\n", "DESAFIO 83".center(40), "\n")

expressao = input("Digite sua expressão: ")  # Recebe a expressão digitada pelo usuário.
abre = 0  # Variavel acumuladora para checar o numero de parenteses abertos.
invalid = False  # Variavel para determinar se a expressão é valida ou inválida.
lista = list()  # Lista para armazenar os parênteses.

for c in expressao:  # Percorre a expressão e extrai os parenteses.
    if c in "()":
        lista.append(c)  # Todo parêntese será adicionado à lista.
if lista.count('(') != lista.count(')'):  # Se a quantidade de "(" e ")" for diferente,
    # já sabemos que a expressão é invalida.
    invalid = True
else:  # Caso contrário é necessário realizar mais alguns filtros.
    for x in lista:  # Será feito o percurso dentro da lista em que os parenteses foram adicionados.
        if x == '(':  # Se o elemento for '(' o acumulador abre recebe +1.
            abre += 1
        elif x == ')':  # Se o elemento for ')' o acumulador abre recebe -1.
            abre -= 1
        if abre == -1:  # Se o elemento da lista for ')', como o abre inicia com 0, recebendo -1 ele irá ficar negativo.
            # O que nos indica que a expressão esta errada, sendo interrompido o resto da checagem.
            invalid = True
            break

# Por fim é informado ao usuário se a expressão digitada por ele é válida ou não.
print("Sua expresão é válida!" if not invalid else "Sua expressão está errada!")
