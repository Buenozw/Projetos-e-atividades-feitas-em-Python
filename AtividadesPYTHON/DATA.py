import oracledb

# Criar uma conexão com banco de dados Oracle
def getConnection():
    try:
        conn = oracledb.connect(user="RM564115",
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
            CREATE TABLE ceo_details(
            id number GENERATED ALWAYS AS IDENTITY,
            first_name VARCHAR(50),
            last_name VARCHAR(50),
            company VARCHAR(30),
            age number (10)
            )
        """
        cursor.execute(sql)
        print(f"Tablea CEO_DETAILS foi criada com sucesso!")
    except oracledb.Error as e:
        print(f"Erro ao criar tabela: {e}")

conn = getConnection()
print(f"Conexão: {conn.version}")
criar_tabela(conn)

print("Fechando a conexão...")
conn.close()

# Operação CRUD
# Create (insert)
def create_ceo(firt_name, last_name, company, age):
    print('*** Inserindo um novo CEO na tabela CEO_DETAILS ***')

    # Obter uma conexão
    conn = getConnection()

    # Validação da conexão
    if not conn:
        return

    try:
        cursor = conn.cursor() # Obter o cursor
        slq = """
            INSERT INTO ceo_details (first_name, last_name, company, age)
            VALUES (:first_name, :last_name, :company, :age)
        """
        cursor.execute(slq, {
            'first_name' : firt_name,
            'last_name' : last_name,
            'company' : company,
            'age' : age
        })
        conn.commit()
        print(f'CEO {firt_name}{last_name} foi adicionado com sucesso!')
    except oracledb as e:
        print(f'Erro ao inserir o CEO {firt_name}{last_name}')
        print(f'Mensagem de erro: {e}')
        conn.rollback() # ele volta
    finally:
        if conn:
            conn.close()

# Exibir os dados de todos os CEOs
# Read (select)

def read_ceos():
    print(f'*** Lê e exibe todos os CEOs da tabela CEO_DETAILS ***')

    conn = getConnection()
    
    if not conn: 
        return
    try:
        sql = """
        SELECT id, first_name, last_name, company, age 
        FROM ceo_details
        """
        cursor = conn.cursor()
        cursor.execute(sql)
        print('------- Lista de CEOs -------')
        rows = cursor.fetchall()
        for row in rows:
            print(f'ID: {row[0]} | Nome: {row[1]} {row[2]} | Empresa: {row[3]} | Idade: {row[4]}')
        print('-------------------------------------------------------')
    except oracledb as e:
        print(f'Erro ao ler os CEOs: {e}')

        