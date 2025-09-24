'''
CRUD - Create, Read, Update e Delete
   - conjunto de operações básicas para manipulação de dados

Módulo (biblioteca) - oracledb (sucessor do cx_oracle)
    - permite que a aplicação Python se conecte ao banco de 
    dados Oracle e execute as instruções SQL

Pré-requisitos
    - instalar a biblioteca oracledb
    - pip install <biblioteca>
    Exemplo: pip install oracledb

String de conexão
<user_name>/<password>@<db_host_address>:<db_port>/<db_service>
Exemplo: "usuario/senha@dominio:1521/orcl"


Tabela - ceo_details
campos - nome, sobrenome, empresa, idade
Exemplo: "Steve", "Jobs", "Apple", 50

'''

import oracledb

#dominio = "oracle.fiap.com.br:1521/orcl"

#criar (obter) uma conexão com o banco de dados Oracle (FIAP)
def getConnection():
    try:
        conn = oracledb.connect(
            user = "RM564115",
            password = "240606",
            host = "oracle.fiap.com.br",
            port = "1521",
            service_name = "orcl"
            #dominio = dominio
        )
        print('Conexão com Oracle DB realizada!')
    except Exception as e:
        print(f'Erro ao obter a conexão: {e}')
    return conn

#criar a tabela ceo_details
def create_table(conn):
    #obter CURSOR - objeto utilizado para executar as instruções SQL
    cursor = conn.cursor()

    try:
        sql = """
            CREATE TABLE ceo_details(
            id number GENERATED ALWAYS AS IDENTITY,
            first_name VARCHAR(30),
            last_name VARCHAR(30),
            company VARCHAR(30),
            age number(10),
            PRIMARY KEY (id)
            )
        """
        cursor.execute(sql)
        print(f'Tabela CEO_DETAILS foi criada com sucesso!')
    except oracledb.Error as e:
        print(f'Erro de conexão: {e}')


#Operações CRUD
def create_ceo(first_name, last_name, company, age):
    print('*** Inserindo um novo CEO na tabela CEO_DETAILS ***')
    conn = getConnection()

    #validação da conexão
    if not conn:
        return
    
    try:
        cursor = conn.cursor() #obter um cursor
        sql = """
            INSERT INTO ceo_details (first_name, last_name, company, age)
            VALUES (:first_name, :last_name, :company, :age)
        """
        cursor.execute(sql, {
            'first_name' : first_name,
            'last_name' : last_name,
            'company' : company,
            'age' : age
        })
        conn.commit()
        print(f'CEO {first_name} {last_name} adicionado com sucesso!')
    except oracledb.Error as e:
        print(f'\nErro ao inserior CEO: {e}')
        conn.rollback()
    finally:
        if conn:
            conn.close()    

#Exibir os dados de todos os CEOs
def read_ceos():
    print('*** Lê e exibe todos os CEOs da tabela ***')
    conn = getConnection()
    if not conn:
        return
    
    try:
        cursor = conn.cursor()
        sql = """
            SELECT id, first_name, last_name, company, age
            FROM ceo_details ORDER BY id
        """
        cursor.execute(sql)
        print("\n --- Lista de CEOs ---")
        rows = cursor.fetchall()
        for row in rows:
            print(f'ID: {row[0]}, Nome: {row[1]} {row[2]}, Empresa: {row[3]}, Idade: {row[4]}')
            print('----------------------------------')
    except oracledb.Error as e:
        print(f'\nErro ao ler CEOs: {e}')
    finally:
        if conn:
            conn.close()
 
#UPDATE
#Atualizar a idade de um CEO

def update_ceo(ceo_id, new_age):
    print(f'*** Atualizando a idade de um CEO com base no ID ***')

    conn = getConnection()
    
    if not conn:
        return
    
    try:
        cursor = conn.cursor()
        sql = "UPDATE ceo_details SET age = :new_age WHERE id = :ceo_id"
        cursor.execute(sql, {'new_age' : new_age, 'ceo_id': ceo_id})
        conn.commit()
        if cursor.rowcount > 0:
            print(f'A idade do CEO {ceo_id} foi atualizada!')
        else:
            print(f'Nenhum CEO com ID {ceo_id} foi encontrado!')
    except oracledb.Error as e:
        print(f'\n Erro ao atualizar a idade: {e}') 
        conn.rollback()
    finally:
        if conn:
            conn.close()

#Delete
# Remove um CEO pelo id

def delete_ceo(ceo_id):
    print(f'*** Excluindo o CEO com id: {ceo_id} ***')

    conn = getConnection()

    if not conn:
        return
    
    try:
        cursor = conn.cursor()
        sql = "DELETE FROM ceo_details WHERE id = :ceo_id"
        cursor.execute(sql, {'ceo_id' : ceo_id})
        conn.commit()
        if cursor.rowcount > 0:
            print(f'CEO com ID {ceo_id} foi excluido!')
        else:
            print(f'Nenhuma CEO com id {ceo_id} foi encontrado!')    
    except oracledb.Error as e:
        print(f'\nErro ao excluir CEO: {e}')
        conn.rollback()
    finally:
        if conn:
            conn.close()

#Menu Principal
def main():

    while True:
        print('*** Menu CRUD - CEO Details ***')
        print('1. Inserir um novo CEO')
        print('2. Listar todos os CEOs')
        print('3. Atualizar a idade de um CEO')
        print('4. Excluir um CEO')
        print('5. Sair')

        opcao = int(input('Digite uma opção: '))
        if opcao == 1:
            first_name = input('Nome: ')
            last_name = input('Sobrenome: ')
            company = input("Empresa :")
            age = int(input('Idade: '))
            create_ceo(first_name, last_name, company, age)
        elif opcao == 2:
            read_ceos()
        elif opcao == 3:
            ceo_id = int(input('Digite o ID do CEO: '))
            new_age = int(input('Digite a nova idade do CEO: '))
            update_ceo(ceo_id, new_age)
        elif opcao == 4:
            ceo_id = int(input('Digite o ID do CEO: '))
            delete_ceo(ceo_id)
        elif opcao == 5:
            print('Encerrando no programa... até breve!')    
            break
        else:
            print('Opção inválida... tente novamente!')







#Programa Principal


#conn = getConnection() #obtendo uma conexão
#print(f'Conexão: {conn.version}')

#create_table(conn)
#create_ceo('Bill', 'Gates', 'Microsoft', 55)
#create_ceo('Wagner', 'Sanches', 'FIAP', 45)
#read_ceos()

#update_ceo(25, 48)
#delete_ceo(25)
#read_ceos()
main()









#update_ceo(3, 100)
#read_ceos()

#delete_ceo(3)
#read_ceos()



#print(f'Fechando a conexão...')
#conn.close()