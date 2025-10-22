import requests
import json

'''
Passo 1: Instalar biblioteca requests
-- abra o terminal (cmd)
-- pip install requests
'''

def consultar_cep(cep):

    url = f'https://viacep.com.br/ws/{cep}/json/'

    print(f'Consultando o CEP {cep}...')
    print(f'-' * 30)

    try:

        response = requests.get(url)

        # 200 indica sucesso (status_code)
        if response.status_code == 200:
            dados_endereco = response.json()

            if 'erro' not in dados_endereco:
                print(f'[ERRO] CEP não encontrado ou inválido!')
                return None
            
            return dados_endereco
        
        else:
            print(f'[ERRO] Falha na consulta do CEP. \nStatus code: {response.status_code}')
            return None
    except Exception as e:
        print(f'[ERRO] Erro...: {e}')
        return None
    
#Programa principal
endereco = consultar_cep('01311000')
print(f' --- Resultado da consulta --- ')
print(f'CEP: {endereco.get("cep")}')
print(f'Logradouro: {endereco.get("logradouro")}')
print(f'Bairro: {endereco.get("bairro")}')
print(f'Cidade/UF: {endereco.get("localidade")}\{endereco.get["uf"]}')
print(f'--- Fim da consulta ---')


        
    