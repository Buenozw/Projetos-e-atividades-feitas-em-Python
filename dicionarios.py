'''
Sistema simplificado de notas de alunos
Contexto: Criar um programa em python para armazenar
o nomee de aluno e suas respectivas notas. O programa
deve ter FUNCOES que permitem adicionar, remover, atualizar e calcular
a media das notas dos alunos.

Usar dicionarios para armazenar os dados dos alunos. -chave sera o nome do aluno
'''

# dicionarios para simular banco de dados
notas_alunos = {
    'Alice': [8.5, 7.0, 9.0],
    'Bob': [6.0, 7.5, 8.0],
    'Charlie': [9.0, 8.5, 10.0]
}
# Função para adicionar um aluno e suas notas
def adicionar_aluno(nome, notas):
   print(f'Adicionando aluno: {nome}')
   if nome not in notas_alunos:
      notas_alunos[nome] = notas
      print(f'Aluno {nome} adicionado com sucesso!')
   else:
      print(f'Aluno {nome} ja existe!')

# Função para remover um aluno
def remover_aluno(nome):
   print(f'Removendo aluno: {nome}')
   if nome in notas_alunos:
      del notas_alunos[nome]
      print(f'Aluno {nome} removido com sucesso!')
   else:
      print(f'Aluno {nome} nao encontrado!')

# Função para atualizar as notas de um aluno
def atualizar_notas(nome, novas_notas):
   print(f'Atualizando notas do aluno: {nome}')
   if nome in notas_alunos:
      notas_alunos[nome].append(novas_notas)
      print(f'Notas do aluno {nome} foram atualizadas')
   else:
      print(f'Aluno {nome} nao encontrado!')

# Função para calcular a média das notas de um aluno
def calcular_media(nome):
   print(f'Calculando media do aluno: {nome}')
   if nome in notas_alunos:
      notas = notas_alunos[nome] # pegando a lista de notas do aluno
      soma = 0
      for nota in notas:
         soma += nota
         cont += 1
      media = soma / cont
      return f'Media do aluno {nome} é: {media:.2f}'
   else: 
      return f'Aluno {nome} nao encontrado!'
   
def listar_alunos():
   print('Lista de alunos e suas notas: ')
   print('--------LISTA DE ALUNOS--------')
   for nome, notas in notas_alunos.items():
      print(f'Aluno: {nome} \nNotas: {notas}')
      print('-------------------------------')

# Programa principal
listar_alunos()
adicionar_aluno('Diana', [7.5, 8.0])
listar_alunos()


remover_aluno('Bob')
listar_alunos()