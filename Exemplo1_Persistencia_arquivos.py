"""
Pensamento Computacional

- Persistência de dados em arquivos
- Deconposição em 3 etapas:
    1. Abrir o arquivo     (pode ser para leitura ou escrita)
    2. Manipular o arquivo (ler ou escrever dados)
    3. Fechar o arquivo    (salvar as informações)

Em Python, essas operações ocorrem através de duas funções:
    - open()  -> abre o arquivo
      Modos de Operação:
        'r' -> (read)  leitura (abre o arquivo existente APENAS para leitura)
        'w' -> (write) escrita (cria um novo arquivo ou sobrescreve o existente)
        'a' -> (append)escrita (abre o aquivo para escrita, adicionando um novo item ao final)
        'b' -> modo binário (imagens, vídeos, etc.)
        '+' -> leitura e escrita
    - close() -> fecha o arquivo
"""

# Exemplo 1: Criar um arquivo e escrever dados nele
# Cadastro de nomes de alunos

ARQUIVO_TEXTO = 'cadastro.txt'

"""Escrever uma lista de strings (nome dos alunos) em 
um arquivo texto - sobrescrevendo os dados anteriores("w")"""
def escrever(dados):
    print(f'Escrevendo os dados no arquivo {ARQUIVO_TEXTO}...')

    try:
        open(ARQUIVO_TEXTO, 'w')  # Abre o arquivo para escrita (sobrescreve)
        with open(ARQUIVO_TEXTO, 'w') as arquivo:
            for item in dados:
                arquivo.write(f'{item}\n')# Escreve cada nome em uma nova linha
        print('Dados escritos com sucesso✅!')
    except Exception as e:
        print(f'Erro ao escrever no arquivo❗: {e}')


"""Ler os dados de um arquivo texto e retornar uma lista de strings"""
def ler():
    print(f'Lendo os dados do arquivo {ARQUIVO_TEXTO}...')

    try:
        with open(ARQUIVO_TEXTO, 'r') as arquivo:
            #Linhas é uma lista []
            linhas = []
            for linha in arquivo.readlines():
                #strip() -> remove espaços em branco e quebras de linha
                linhas.append(linha.strip())
                #Remove espaços em branco e quebras de linha
        return linhas             
    except FileNotFoundError:
        return []  # Retorna uma lista vazia se o arquivo não existir
    except Exception as e:
        print(f'Erro ao ler o arquivo❗: {e}')
        return []


"""Adicionar um novo dado ao final do arquivo texto"""
def adicionar(novo_dado):
    print(f'Adicionando o dado no arquivo {ARQUIVO_TEXTO}...')

    try:
        with open(ARQUIVO_TEXTO, 'a') as arquivo:
            arquivo.write(f'{novo_dado}\n')  # Adiciona o novo nome no final do arquivo
        print('Dado adicionado com sucesso✅!')
    except Exception as e:
        print(f'Erro ao adicionar no arquivo❗: {e}')

def menu():
    print("\n--- Persistencia de dados em Arquivos ---")
    print("\n----Menu de Opções👌:")
    print("1. Ler dados do arquivo")
    print("2. Ler dados existentes no arquivo")
    print("3. Adicionar novo dado ao arquivo")
    print("4. Sair")
    escolha = input("Escolha uma opção (1-4): ")

    if escolha == '1':
        dados_brutos = input("Digite os nomes dos alunos separados por vírgula: ")
        dados = dados_brutos.split(',')
        dados_limpos = []
        for dados in dados:
            dados_limpos.append(item.strip())

            escrever(dados_limpos)
    elif escolha == '2':
        dados = ler()
        if dados:
            print("Dados lidos do arquivo:")
            for item in dados:
                print(f'- {item}')
        else:
            print("O arquivo está vazio ou não existe.")
    elif escolha == '3':
        novo_dado = input("Digite o novo dado: ")
        adicionar(novo_dado)
    elif escolha == '4':
        print("Saindo do programa. Até mais!")
        return
    else:
        print("Opção inválida. Tente novamente.")

# Programa Principal
if __name__ == "__main__":
    while True:
        menu()

