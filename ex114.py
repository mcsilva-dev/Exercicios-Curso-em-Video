"""Crie um código em python que teste se o site Pudim está acessivel pelo computador usado."""

from requests import get

print('\n', 'DESAFIO 114'.center(38), '\n')

try:
    get('http://pudim.com.br/')
except Exception as erro:
    print(erro.__class__)
else:
    print('\033[0;32mConsegui acessar o site do Pudim com sucesso!\033[m')
