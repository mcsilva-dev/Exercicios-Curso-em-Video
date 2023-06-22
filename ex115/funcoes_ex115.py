from time import sleep

cores = {
    'amarelo': '\033[1;33;3m',
    'azul': '\033[1;36;3m',
    'vermelho': '\033[1;31;3m',
    'limpa': '\033[m'
}


def linha(tam=50):
    return '-' * tam


def opcoes():
    return f"""{cores['amarelo']}1{cores['limpa']} - {cores['azul']}Ver pessoas cadastradas{cores['limpa']}
{cores['amarelo']}2{cores['limpa']} - {cores['azul']}Cadastrar nova Pessoa{cores['limpa']}
{cores['amarelo']}3{cores['limpa']} - {cores['azul']}Sair do sistema{cores['limpa']}"""


def menu(text):
    print(linha())
    print(f'{text}'.center(50))
    print(linha())
    if text == 'MENU PRINCIPAL':
        print(opcoes())


def cadastradas():
    menu('PESSOAS CADASTRADAS')
    try:
        arquivo = open('pessoas cadastradas.txt', 'r')
        for pessoa in arquivo.readlines():
            p = pessoa.split(';')
            nome = p[0]
            idade = p[1]
            print(f"{nome:<40}{idade} anos")
        arquivo.close()
    except FileNotFoundError:
        print(f"{cores['vermelho']}Erro: ainda não há nenhuma pessoa registrada.{cores['limpa']}")
    sleep(1)


def cadastrar():
    menu('NOVO CADASTRO')
    arquivo = open('pessoas cadastradas.txt', 'a')
    pessoa = dict()
    while True:
        try:
            while True:
                pessoa['nome'] = ' '.join(str(input('Nome: ')).title().split())
                if pessoa['nome'].replace(' ', '').isalpha():
                    break
                else:
                    raise ValueError
        except ValueError:
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
    for valor in pessoa.values():
        arquivo.write(f'{valor}')
        arquivo.write(';')
    arquivo.write('\n')
    print(f"{pessoa['nome']} foi cadastrado(a) com sucesso!")
    sleep(1)
    arquivo.close()
