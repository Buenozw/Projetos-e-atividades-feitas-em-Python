while True:
    try:
        n1 = int(input('numero: '))
        n2 = int(input('Numero: '))
        result = n1/n2
        print('O 4esultado: {result}')
    except ZeroDivisionError:
        print('nao pode ser dividido por ZERO')
    except ValueError:
        print('Entrada invalida! Por favor, digite um numero')
