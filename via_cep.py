import requests
import json

'''
Passo 1: Instalar biblioteca requests
-- abra o terminal (cmd)
-- pip install requests
'''

def buscar_cep(cep):

    url = f'https://viacep.com.br/ws/{cep}/json/'

    print(f'Consultando o CEP {cep}...')
    print(f'-' * 30)

    try:

        response = requests.get(url)
    