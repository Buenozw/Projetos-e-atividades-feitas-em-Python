import time

def selection_sort(lista):
    """
    Ordena uma lista usando o algoritmo de ordenação por seleção.

    """
    n = len(lista)# Obter o tamanho da lista

    for i in range(n):
        indice_minimo = i  # Assume o primeiro elemento não ordenado como o menor
        
        for j in range (i + 1, n):
            if lista[j] < lista[indice_minimo]:
                indice_minimo = j # Atualiza o índice do menor elemento
        
        # realiza a troca (atribuição paralela)
        lista[i], lista[indice_minimo] = lista[indice_minimo], lista[i]
    return lista

def tempo():
    print(f'Inicio...')
    inicio = time.time()
    for i in range(10):
        print('.')
        time.sleep(1)
    fim = time.time()
    print(f'Fim...')
    print(f'Tempo: {fim - inicio} segundos')  

#Programa principal
lista = [64, 25, 12, 22, 11]
print(f'Lista Original: {lista}')
inicio = time.time()
selection_sort(lista)
fim = time.time()
print(f'Lista Ordenada: {lista}')
