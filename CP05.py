"""
-------- CP05 ---------
--TIPO: PROVA PRÁTICA--

--NOMES DOS INTEGRANTES
--Aluno 1: [Joao Victor Bueno] RM: 564115
--Aluno 2: [Joao Victor Caetano] RM: 562074
--Aluno 3: [Felipe Furlanetto] RM: 562766

--DESCRIÇÃO DO PROGRAMA
  O programa desenvolvido tem como objetivo comparar o desempenho de diferentes algoritmos de ordenação em Python,
analisando seus tempos médios de execução sobre listas de tamanhos variados.
  O sistema permite que o usuário escolha interativamente qual algoritmo deseja utilizar (Bubble Sort, Selection Sort, Insertion Sort ou Merge Sort)
para ordenar uma lista de números inteiros lida a partir de um arquivo de entrada. Após a ordenação, a lista é salva em um novo arquivo de saída, 
preservando os resultados de forma organizada.
  Além da interação com o usuário, o programa realiza testes automatizados de desempenho, 
medindo o tempo médio de execução de cada algoritmo para listas com tamanhos crescentes. 
Os resultados são exibidos em uma tabela comparativa e representados graficamente através de um gráfico de linha gerado com o Matplotlib, 
facilitando a visualização da eficiência de cada método.

--CONFIGURAÇÕES DO PROGRAMA
--Processador : AMD Ryzen 7 5700
--RAM : 24 GB
--Sistema Operacional : Windows 11 Pro
--Versão do Python : 3.11.4
--Placa de vídeo : AMD Radeon RX 5500 XT

"""
# Importação das bibliotecas utilizadas
import time
import sys
import random
import pandas as pd
import matplotlib.pyplot as plt

# -------FUNÇÕES DE ORDENAÇÃO-------

def bubble_sort(lista):
    """
    Ordena uma lista de números usando o método Bubble Sort.
    Percorre a lista repetidamente, comparando elementos adjacentes
    e trocando-os se estiverem na ordem incorreta.
    Complexidade: O(n²)
    """
    tam = len(lista)
    for i in range(tam - 1):
        troca = False  # flag de controle
        for j in range(0, tam - i - 1):
            if lista[j] > lista[j + 1]:
                # realiza a troca
                troca = True
                # atribuição paralela
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
        # se não for necessario realizar a troca, o programa
        # irá sair do loop
        if not troca: 
            return lista

def selection_sort(lista):
    """
    Ordena uma lista usando o método Selection Sort.
    A cada iteração, encontra o menor elemento e o move para a posição correta.
    Complexidade: O(n²)
    """
    n = len(lista)
    for i in range(n):
        indice_minimo = i
        # Encontra o índice do menor elemento no restante da lista
        for j in range(i + 1, n):
            if lista[j] < lista[indice_minimo]:
                indice_minimo = j
        # Troca o elemento atual com o menor encontrado
        lista[i], lista[indice_minimo] = lista[indice_minimo], lista[i]
    return lista

def insertion_sort(lista):
    """
    Ordena uma lista usando o método Insertion Sort.
    Insere cada elemento na posição correta em relação aos anteriores.
    Complexidade: O(n²)
    """
    for i in range(1, len(lista)):
        pivo = lista[i]
        j = i - 1
        # Desloca os elementos maiores que o pivo uma posição à frente
        while j >= 0 and pivo < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        # Insere o pivo na posição correta
        lista[j + 1] = pivo
    return lista

def merge_sort(lista):
    """
    Ordena uma lista usando o método Merge Sort (recursivo).
    Divide a lista em duas partes, ordena cada uma e as combina.
    Complexidade: O(n log n)
    """
    if len(lista) > 1:
        meio = len(lista) // 2

        # fatiamento da lista
        L = lista[:meio]  # metade esquerda
        R = lista[meio:]  # metade direita

        # chamada recursiva em cada metade
        merge_sort(L)
        merge_sort(R)

        # variaveir de controle
        # i - fará o controle da lista esquerda L
        # j - fará o controle da lista direita R
        # k - fará o controle da lista anterior à recursão
        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                lista[k] = L[i]
                i += 1
            else:
                lista[k] = R[j]
                j += 1
            k += 1

        # verificação dos elementos da lista esquerda
        while i < len(L):
            lista[k] = L[i]
            i += 1
            k += 1

        # verificação dos elementos da lista direita
        while j < len(R):
            lista[k] = R[j]
            j += 1
            k += 1
    return lista

# ======================== ENTRADA E SAÍDA DE ARQUIVOS ========================

def ler_lista_arquivo(arquivo_entrada):
    """
    Lê uma lista de números inteiros de um arquivo de texto.
    Retorna uma lista contendo os valores.
    """
    with open(arquivo_entrada, 'r') as f:
        conteudo = f.read()
        return [int(x) for x in conteudo.split()]

def salvar_lista_arquivo(arquivo_saida, lista):
    """
    Salva a lista ordenada em um arquivo de saída (.txt),
    incluindo cabeçalho e rodapé para identificação.
    """
    with open(arquivo_saida, 'w') as f:
        f.write("===LISTA ORDENADA=== \n")
        for item in lista:
            f.write(f"\n{item}")
        f.write(f"\n===FIM DA LISTA ORDENADA===\n")

# ======================== CRONOMETRAGEM DE ALGORITMOS ========================

def medir_tempo(algoritmo, n):
    """
    Mede o tempo de execução de um algoritmo de ordenação.
    Executa 3 vezes com listas aleatórias e retorna as amostras e a média.
    """
    tempos = []
    for _ in range(3):  # 3 amostras
        lista = [random.randint(0, 10000) for _ in range(n)]
        inicio = time.time()     # Marca o início
        algoritmo(lista.copy())  # Usa uma cópia da lista
        fim = time.time()        # Marca o fim
        tempos.append(fim - inicio) # Registra o tempo decorrido
    media = sum(tempos) / len(tempos)
    return tempos, media


# ======================== EXECUÇÃO DOS TESTES AUTOMÁTICOS ========================

def executar_testes():
    """
    Executa testes automáticos com diferentes tamanhos de listas,
    aplicando todos os algoritmos e registrando o tempo médio de execução.
    Também gera um gráfico comparativo com os resultados obtidos.
    """
    # Tamanhos das listas usadas nos testes
    tamanhos = [1000, 5000, 10000, 25000, 50000]
    # Algoritmos disponíveis
    algoritmos = {
        'Bubble Sort': bubble_sort,
        'Selection Sort': selection_sort,
        'Insertion Sort': insertion_sort,
        'Merge Sort': merge_sort
    }

    resultados = [] # Lista que armazenará os resultados
    
    # Executa cada algoritmo para cada tamanho de lista
    for nome, func in algoritmos.items():
        for n in tamanhos:
            tempos, media = medir_tempo(func, n)
            resultados.append({
                'Algoritmos': nome,
                'N': n,
                'Amostra 1(s)': tempos[0],
                'Amostra 2(s)': tempos[1],
                'Amostra 3(s)': tempos[2],
                'Média (s)': media
            })
            print(f"{nome:<15} | N={n:<6} | Média: {media:.4f}s")

    # Cria DataFrame com os resultados
    df = pd.DataFrame(resultados)
    print("\n======================= TABELA DE RESULTADOS ============================\n")
    print(df.to_string(index=False))

    # Gera o gráfico comparativo
    plt.figure(figsize=(10, 6))
    for nome in algoritmos.keys():
        df_alg = df[df['Algoritmos'] == nome]
        plt.plot(df_alg['N'], df_alg['Média (s)'], marker='o', label=nome)

    plt.title('Comparativo de Tempo Médio de Execução')
    plt.xlabel('Tamanho da Lista(N)')
    plt.ylabel('Tempo Médio(segundos)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    return df

# ======================== MENU INTERATIVO ========================

def main():
    print("\n============ MENU DE ALGORITIMOS DE ORDENAÇÃO📈 =================")
    print("Menu interativo para o usuário escolher o algoritmo de ordenação.")
    print("\n[1] Bubble Sort")
    print("[2] Selection Sort")
    print("[3] Insertion Sort")
    print("[4] Merge Sort")

    escolha = input("\nEscolha o algorítimo de ordenação (1-4): ")
    arquivo_entrada = input("\nDigite o nome do arquivo de entrada: ")
    arquivo_saida = input("Digite o nome do arquivo de saída: ")
    
    # Lê a lista de números do arquivo de entrada
    lista = ler_lista_arquivo(arquivo_entrada)
    
    # Escolhe o algoritmo conforme a opção selecionada
    if escolha == '1':
        lista_ordenada = bubble_sort(lista)
    elif escolha == '2':
        lista_ordenada = selection_sort(lista)
    elif escolha == '3':
        lista_ordenada = insertion_sort(lista)
    elif escolha == '4':
        lista_ordenada = merge_sort(lista)
    else:
        print("Escolha inválida!, por favor selecione uma opção entre 1 e 4.")
        sys.exit(1)
    
    # Salva a lista ordenada no arquivo de saída
    salvar_lista_arquivo(arquivo_saida, lista_ordenada)
    print("\nLista ordenada salva em {arquivo_saida}\n")

# ======================== EXECUÇÃO DO PROGRAMA ========================
if __name__ == "__main__":
    main()
    executar_testes()
    


 