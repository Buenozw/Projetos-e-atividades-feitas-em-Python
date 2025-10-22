"""
Recursão em Python - conceito de programação onde uma função
chama a si mesma para resolver um problema.

Componetes principais:

1. Caso base: condição que encerra a recursão.
2. Chamada recursiva: a função chama a si mesma
   com um argumento modificado.

menu() >>> add() >>> menu() >>> sub() >>> menu() >>> mult()
"""

#Exemplo 1 - Somatório de todos os elementos de uma lista
def somatorio(lista):
    if len(lista) == 1: # Caso base
        return lista[0]
    else:
        return lista[0] + somatorio(lista[1:])  # Chamada recursiva
    
#Exemplo 2 - Calculo Fatorial de um número - 5! = 5 * 4 * 3 * 2 * 1 = 120
# Caso base: -> n == 1 ou 0! = 1
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)
    
#Programa principal
#lista = [1, 2, 3, 4, 5]
#print(f'Soma: {somatorio(lista)}')
print(f'Fatorial: {fatorial(5)}')