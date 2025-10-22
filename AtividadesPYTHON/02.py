try:
    lista = [1, 2, 3]

    print('--FOR--')
    for i in lista:
       print(f'Elemento: {i}')
    print('--WHILE--')
    i = 0
    while i<=3:
       print(f'Elemento: {lista[i]}')
    i+=1
except IndentationError:
   print('Erro: indice fora da lista')
except IndexError:
   print('Erro: indice fora da lista')
except Exception as e:
   print(f'Erro genérico: {e}')