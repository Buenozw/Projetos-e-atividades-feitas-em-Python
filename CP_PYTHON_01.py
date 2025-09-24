# Nomes: Felipe Furlanetto, João Victor Bueno Castelini da Silva e João Victor Caetano Alves da Silva.
# Turma: 1TDSPF

import random

# Função para criar o tabuleiro oculto com bombas
def criar_tabuleiro(linhas, colunas, num_bombas):
    tabuleiro = [[" " for _ in range(colunas)]
                 for _ in range(linhas)]
    bombas = 0
    while bombas < num_bombas:
        i = random.randint(0, linhas - 1)
        j = random.randint(0, colunas - 1)
        if tabuleiro[i][j] != "💣":
            tabuleiro[i][j] = "💣"
            bombas += 1
    return tabuleiro

# Função para contar bombas ao redor de uma célula
def contar_bombas(tabuleiro, i, j):
    linhas, colunas = len(tabuleiro), len(tabuleiro[0])
    contador = 0
    for x in range(max(0, i - 1), min(linhas, i + 2)):
        for y in range(max(0, j - 1), min(colunas, j + 2)):
            if tabuleiro[x][y] == "💣":
                contador += 1
    return contador

# Função para exibir o tabuleiro visível do jogador com índices
def exibir_tabuleiro(tabuleiro_visivel):
    
    colunas = len(tabuleiro_visivel[0])
    linhas = len(tabuleiro_visivel)

    # Cabeçalho com os números das colunas
    print("   ", end="")
    for numero_coluna in range(colunas):
        print(numero_coluna, end=" ")
    print()

    # Cada linha com seu índice
    for numero_da_linha in range(linhas):
        print(numero_da_linha, " ", end="")
        print(*tabuleiro_visivel[numero_da_linha])
    print()

# Função principal do jogo
def jogar_campo_minado():
    linhas, colunas, bombas = 10, 10, 7
    tabuleiro = criar_tabuleiro(linhas, colunas, bombas)
    tabuleiro_visivel = [["■" for _ in range(colunas)] for _ in range(linhas)]
    casas_abertas = 0
    total_casas = linhas * colunas - bombas
    
    print('\n[💣--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------💣]')
    print("\n[✅======================================================================== BEM VINDO(A) AO CAMPO MINADO! ===========================================================================================✅]")
    print('\n[💣--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------💣]')
    print("\nOBJETIVO: Revelar todas as células sem bombas.")
    print("\nCOMANDOS: Digite as coordenadas (linha e coluna) para revelar uma célula.")
    print("\nBOA SORTE!\n")
    exibir_tabuleiro(tabuleiro_visivel)

    while True:
        try:
            i = float(input("Digite a linha (0 a 6): "))
            j = int(input("Digite a coluna (0 a 6): "))
        except ValueError:
            print("\nEntrada inválida! Digite números inteiros.")
            i, j = -1, -1
        if i < 0 or j < 0 or i >= linhas or j >= colunas:
            print("\nPosição fora do tabuleiro!")
        else:
            if tabuleiro[i][j] == "💣":
                print("\n💥 Você encontrou uma bomba😥! Fim de jogo.")
                exibir_tabuleiro(tabuleiro)
                break
            else:
                bombas_proximas = contar_bombas(tabuleiro, i, j)
                tabuleiro_visivel[i][j] = str(bombas_proximas)
                casas_abertas += 1
            exibir_tabuleiro(tabuleiro_visivel)
            if casas_abertas == total_casas:
                print("\nPARABÉNS, VOCÊ VENCEU O JOGO❗✅")
                exibir_tabuleiro(tabuleiro)
                break

# Executa o jogo
jogar_campo_minado()