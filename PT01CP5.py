import oracledb

def get_conexao():
    try:
        conn = oracledb.connect(
            user="RM564115",                  
            password="240606",                 
            host="oracle.fiap.com.br",
            port="1521",
            service_name="orcl"
        )  
    except Exception as e:
        print(f"Erro ao obter a conexão: {e}")
    return conn

def criar_tabela(conn):
    cursor = conn.cursor()
    try:
        sql = """
            CREATE TABLE INFO_PRODUTOS(
            id NUMBER,
            nome VARCHAR(50) NOT NULL,
            descricao VARCHAR(100),
            fornecedor VARCHAR(30),
            preco NUMBER(10,2),
            PRIMARY KEY (id)
            )
        """
        cursor.execute(sql)
        print(f"Tabela INFO_PRODUTOS foi criada com sucesso!")
    except oracledb.Error as e:
        print(f"Erro ao criar tabela: {e}")
conn = get_conexao()
print(f"Conexão: {conn.version}")
criar_tabela(conn)
print("Fechando a conexão...")
conn.close() 

def inserir_produto(id, nome, descricao, fornecedor, preco):
    print('--- Inserindo um novo produto na tabela INFO_PRODUTOS ---')
    conn = get_conexao()
    if not conn:
        return
    try:
        cursor = conn.cursor()
        sql = """
            INSERT INTO INFO_PRODUTOS (id, nome, descricao, fornecedor, preco)
            VALUES (:id, :nome, :descricao, :fornecedor, :preco)
            """
        cursor.execute(
        sql, {
            'id' : id,
            'nome' : nome,
            'descricao' : descricao,
            'fornecedor' : fornecedor,
            'preco' : preco
        })
        conn.commit()
        print(f'Produto {nome} adicionado com sucesso!')
    except oracledb.Error as e:
        print(f'\nErro ao inserir o produto: {e}')
        print(f'Mensagem de erro: {e}')
        conn.rollback()
    finally:
        if conn:
            conn.close()

def listar_produtos():
    print('--- Exibe os produtos da tabela INFO_PRODUTOS ---')
    conn = get_conexao()
    if not conn:
        return
    try:
        cursor = conn.cursor()
        sql = """
            SELECT id, nome, descricao, fornecedor, preco
            FROM INFO_PRODUTOS ORDER BY id
            """
        cursor.execute(sql)
        print("\n --- Lista de Produtos ---")
        rows = cursor.fetchall()
        for row in rows:
            print(f'ID: {row[0]}, Nome: {row[1]}, Descrição: {row[2]}, Fornecedor: {row[3]}, Preço: {row[4]}')
            print('----------------------------------')
    except oracledb.Error as e:
        print(f'\nErro ao ler produtos: {e}')
    finally:
        if conn:
            conn.close()

def buscar_produto_por_id(id):
    print(f'--- Buscando produto com ID {id} ---')
    conn = get_conexao()
    if not conn:
        return
    try:
        cursor = conn.cursor()
        sql = """
            SELECT id, nome, descricao, fornecedor, preco
            FROM INFO_PRODUTOS
            WHERE id = :id
            """
        cursor.execute(sql, {'id': id})
        row = cursor.fetchone()
        if row:
            print(f'ID: {row[0]}, Nome: {row[1]}, Descrição: {row[2]}, Fornecedor: {row[3]}, Preço: {row[4]}')
        else:
            print(f'Produto com ID {id} não encontrado.')
    except oracledb.Error as e:
        print(f'\nErro ao buscar produto: {e}')
    finally:
        if conn:
            conn.close()

def atualizar_preco_produto(id, novo_preco):
    print(f'--- Atualizando o preço do produto com ID {id} ---')
    conn = get_conexao()
    if not conn:
        return
    try:
        cursor = conn.cursor()
        sql = """
            UPDATE INFO_PRODUTOS
            SET preco = :novo_preco
            WHERE id = :id
            """
        cursor.execute(sql, {'novo_preco': novo_preco, 'id': id})
        conn.commit()
        if cursor.rowcount > 0:
            print(f'O preço do produto {id} foi atualizado para {novo_preco}!')
        else:
            print(f'Nenhum produto com ID {id} foi encontrado!')
    except oracledb.Error as e:
        print(f'\nErro ao atualizar o preço: {e}')
    finally:
        if conn:
            conn.close()

def deletar_produto(id):
    print(f'--- Excluindo o produto com id: {id} ---')
    conn = get_conexao()
    if not conn:
        return
    try:
        cursor = conn.cursor()
        sql = """
            DELETE FROM INFO_PRODUTOS
            WHERE id = :id
            """
        cursor.execute(sql, {'id': id})
        conn.commit()
        if cursor.rowcount > 0:
            print(f'Produto com id {id} foi excluído!')
        else:
            print(f'Nenhum produto com id {id} foi encontrado!')
    except oracledb.Error as e:
        print(f'\nErro ao excluir produto: {e}')
    finally:
        if conn:
            conn.close()

def main():
    while True:
        print('\n----------------------------------')
        print('------- Menu INFO_PRODUTOS -------')
        print('----------------------------------')
        print('[1]. Inserir um novo produtos')
        print('[2]. Listar todos os produtos')
        print('[3]. Atualizar o preço de um produto')
        print('[4]. Excluir um produto')
        print('[5]. Sair')
        escolha = int(input('Escolha uma opção: '))
        if escolha == 1:
            print('--- Inserir um novo produto ---')
            id = int(input('ID: '))
            nome = input('Nome: ')
            descricao = input('Descrição: ')
            fornecedor = input('Fornecedor: ')
            preco = float(input('Preço: '))
            inserir_produto(id, nome, descricao, fornecedor, preco)
        elif escolha == 2:
            listar_produtos()
        elif escolha == 3:
            print('--- Atualizar o preço de um produto ---')
            id = int(input('ID do produto: '))
            novo_preco = float(input('Novo preço: '))
            atualizar_preco_produto(id, novo_preco)
        elif escolha == 4:
            print('--- Excluir um produto ---')
            id = int(input('ID do produto: '))
            deletar_produto(id)
        elif escolha == 5:
            print('Saindo do programa...')
            print('Conexão fechada.')
            break
main()

             
