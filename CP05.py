"""
--CP05 --
--TIPO: PROVA PRÁTICA--

--NOMES DOS INTEGRANTES
--Aluno 1: [Joao Victor Bueno]
--Aluno 2: [Joao Victor Caetano]
--Aluno 3: [Felipe Furlanetto]

--DESCRIÇÃO DO PROGRAMA


--CONFIGURAÇÕES DO PROGRAMA
--Processador : AMD Ryzen 7 5700
--RAM : 24 GB
--Sistema Operacional : Windows 11 Pro
--Versão do Python : 3.11.4
--Placa de vídeo : AMD Radeon RX 5500 XT

"""

import time
import sys
import random
import pandas as pd
import matplotlib.pyplot as plt

# -------FUNÇÕES DE ORDENAÇÃO-------

def bubble_sort(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range (i + 1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista

def insertion_sort(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        while j >= 0 and chave < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = chave
    return lista

def merge_sort(lista):
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

def ler_lista_arquivo(arquivo_entrada):
    with open(arquivo_entrada, 'r') as f:
        conteudo = f.read()
        return [int(x) for x in conteudo.split()]
    
def salvar_lista_arquivo(arquivo_saida, lista):
    with open(arquivo_saida, 'w') as f:
        for item in lista:
            f.write(f"{item}\n")

# ------FUNÇÕES DE CRONOMETRAGEM-------

def medir_tempo(algoritmo, n):
    tempos = []
    for _ in range(3):  # 3 amostras
        lista = [random.randint(0, 10000) for _ in range(n)]
        inicio = time.time()
        algoritmo(lista.copy())  # Usa uma cópia da lista
        fim = time.time()
        tempos.append(fim - inicio)
    media = sum(tempos) / len(tempos)
    return tempos, media

# ----------- EXECUÇÃO DOS TESTES -------------

def executar_testes():
    tamanhos = [1000, 5000, 10000, 25000, 50000]
    algoritimos = {
        'Bubble Sort': bubble_sort,
        'Selection Sort': selection_sort,
        'Insertion Sort': insertion_sort,
        'Merge Sort': merge_sort
    }

    resultados = []

    for nome, func in algoritimos.items():
        for n in tamanhos:
            tempos, media = medir_tempo(func, n)
            resultados.append({
                'Algoritimos': nome,
                'N': n,
                'Amostra 1 (s)': tempos[0],
                'Amostra 2 (s)': tempos[1],
                'Amostra 3 (s)': tempos[2],
                'Média (s)': media
            })
            print(f"{nome:<15} | N={n:<6} | Média: {media:.4f}s")

    # Cria DataFrame com os resultados
    df = pd.DataFrame(resultados)
    print("\n=== TABELA DE RESULTADOS ===")
    print(df.to_string(index=False))

# ------------------ GRÁFICO COMPARATIVO ------------------

    plt.figure(figsize=(10, 6))
    for nome in algoritimos.keys():
        df_alg = df[df['Algoritimos'] == nome]
        plt.plot(df_alg['N'], df_alg['Média (s)'], marker='o', label=nome)

    plt.title('Comparativo de Tempo Médio de Execução')
    plt.xlabel('Tamanho da Lista (N)')
    plt.ylabel('Tempo Médio (segundos)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    return df
    
# -----Programa principal-----

def main():
    print("======== MENU DE ALGORITIMOS DE ORDENAÇÃO ========")
    print("Menu interativo para o usuário escolher o algoritmo de ordenação.")
    print("[1]. Bubble Sort")
    print("[2]. Selection Sort")  
    print("[3]. Insertion Sort")
    print("[4]. Merge Sort")

    escolha = input("Escolha o algorítimo de ordenação (1-4): ")

    arquivo_entrada = input("Digite o nome do arquivo de entrada: ")
    arquivo_saida = input("Digite o nome do arquivo de saída: ")

    lista = ler_lista_arquivo(arquivo_entrada)

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

    salvar_lista_arquivo(arquivo_saida, lista_ordenada)
    print(f"Lista ordenada salva em {arquivo_saida}")

# EXECUÇÃO DO PROGRAMA
if __name__ == "__main__":
    df_resultados = executar_testes()



