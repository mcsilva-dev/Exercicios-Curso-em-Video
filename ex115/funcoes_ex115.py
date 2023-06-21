from time import sleep

cores = {
    'vermelho': '\033[1;31;3m',
    'limpa': '\033[m'
}


def cadastradas():
    print('-' * 50)
    print('PESSOAS CADASTRADAS'.center(50))
    print('-' * 50)
    try:
        arquivo = open('pessoas cadastradas.txt', 'r')
        for pessoa in arquivo.readlines():
            p = pessoa.split()
            nome = []
            idade = 0
            for i in p:
                if i.isalpha():
                    nome.append(i)
                if i.isdigit():
                    idade = i
            print(f"{' '.join(nome):<40}{idade} anos")
        arquivo.close()
    except FileNotFoundError:
        print(f"{cores['vermelho']}Erro: ainda não há nenhuma pessoa registrada.{cores['limpa']}")
    sleep(2)


def cadastrar():
    print('-' * 50)
    print('NOVO CADASTRO'.center(50))
    print('-' * 50)
    arquivo = open('pessoas cadastradas.txt', 'a')
    pessoa = dict()
    while True:
        try:
            while True:
                pessoa['nome'] = ' '.join(str(input('Nome: ')).title().strip().split())
                if pessoa['nome'].replace(' ', '').isalpha():
                    break
                else:
                    print(f"{cores['vermelho']}Erro: O nome deve ser composto apenas por letras.{cores['limpa']}")
        except KeyboardInterrupt:
            print(f"{cores['vermelho']}O usuário preferiu não informar o nome.{cores['limpa']}")
            pessoa['nome'] = '<desconhecido>'
            break
        else:
            break
    while True:
        try:
            pessoa['idade'] = int(input('Idade: '))
        except (ValueError, TypeError):
            print(f"{cores['vermelho']}Erro: digite um número inteiro.{cores['limpa']}")
        except Exception as erro:
            print(f"{cores['vermelho']}Ocorreu um erro: {erro.__class__}.{cores['limpa']}")
        except KeyboardInterrupt:
            print(f"{cores['vermelho']}O usuário preferiu não informar a idade.{cores['limpa']}")
            pessoa['idade'] = 0
            break
        else:
            break
    for key, valor in pessoa.items():
        arquivo.write(f'{key}: {valor} ')
    arquivo.write('\n')
    print(f"{pessoa['nome']} foi cadastrado(a) com sucesso!")
    sleep(2)
    arquivo.close()

