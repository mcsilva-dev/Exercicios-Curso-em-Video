"""Crie um código em python que teste se o site Pudim está acessivel pelo computador usado."""

import requests.exceptions
from requests import get

print('\n', 'DESAFIO 114'.center(38), '\n')

try:
    get('http://pudim.com.br/')
except requests.exceptions.ConnectionError:
    print('O site pudim não está acessível no momento.')
else:
    print('\033[0;32mConsegui acessar o site do Pudim com sucesso!\033[m')
