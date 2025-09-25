import oracledb

# ------------------- FUNÇÕES DE CONEXÃO -------------------
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
        print(f"Erro ao obter a conexão❗: {e}")
    return conn

# ------------------- CRIAÇÃO DE TABELAS -------------------
def criar_tabela(conn):
    cursor = conn.cursor()
    try:
        sql = """
            CREATE TABLE PACIENTES(
            id_paciente   NUMBER GENERATED ALWAYS AS IDENTITY,
            nome_paciente VARCHAR(50) NOT NULL,
            cpf_paciente  VARCHAR(14) NOT NULL,
            idade_paciente  INTEGER,
            sexo_paciente VARCHAR (40),
            PRIMARY KEY (id_paciente)
            )
        """
        cursor.execute(sql)
        print(f"Tabela PACIENTES foi criada com sucesso✅!")
    except oracledb.Error as e:
        erro, = e.args
        if erro.code == 955:
            print("Tabela PACIENTES já existe ✔️")
        else:
            print(f"Erro ao criar tabela❗: {e}")
conn = get_conexao()
print(f"Conexão: {conn.version}")
criar_tabela(conn)
conn.close()
# Cria a tabela PACIENTES (se não existir)

def criar_tabela_consulta(conn):
    cursor = conn.cursor()
    try:
        sql = """
            CREATE TABLE CONSULTAS(
            id_consulta   NUMBER GENERATED ALWAYS AS IDENTITY,
            nome_consulta VARCHAR(50) NOT NULL,
            descricao_consulta  VARCHAR(100),
            dataHora_consulta  TIMESTAMP,
            id_paciente NUMBER(6) NOT NULL,
            PRIMARY KEY (id_consulta)
            )
        """
        cursor.execute(sql)
        print(f"Tabela CONSULTAS foi criada com sucesso✅!")
    except oracledb.Error as e:
        erro, = e.args
        if erro.code == 955:
            print("Tabela CONSULTAS já existe ✔️")
        else:
            print(f"Erro ao criar tabela❗: {e}")
conn = get_conexao()
print(f"Conexão: {conn.version}")
criar_tabela_consulta(conn)
conn.close()
# Cria a tabela CONSULTAS (se não existir)

def criar_tabela_exame(conn):
    cursor = conn.cursor()
    try:
        sql = """
            CREATE TABLE EXAMES(
            id_exame   NUMBER GENERATED ALWAYS AS IDENTITY,
            nome_exame VARCHAR(50) NOT NULL,
            descricao_exame  VARCHAR(100),
            dataHora_exame  TIMESTAMP,
            id_paciente NUMBER(6) NOT NULL,
            PRIMARY KEY (id_exame)
            )
        """
        cursor.execute(sql)
        print(f"Tabela EXAMES foi criada com sucesso✅!")
    except oracledb.DatabaseError as e:
        erro, = e.args
        if erro.code == 955:
            print("Tabela EXAMES já existe ✔️")
        else:
            print(f"Erro ao criar tabela ❗: {e}")
conn = get_conexao()
print(f"Conexão: {conn.version}")
criar_tabela_exame(conn)
print("Fechando a conexão...")
conn.close()
# Cria a tabela EXAMES (se não existir)

# ------------------- INSERÇÃO DE DADOS -------------------
def inserir_paciente(nome_paciente, cpf_paciente, idade_paciente, sexo_paciente):
    print('\n--------- Inserindo um novo paciente na tabela PACIENTES --------')
    conn = get_conexao()
    if not conn:
        return
    try:
        cursor = conn.cursor()
        sql = """
            INSERT INTO PACIENTES (nome_paciente, cpf_paciente, idade_paciente, sexo_paciente)
            VALUES (:nome_paciente, :cpf_paciente, :idade_paciente, :sexo_paciente)
            """
        cursor.execute(
            sql, {

                'nome_paciente': nome_paciente,
                'cpf_paciente': cpf_paciente,
                'idade_paciente': idade_paciente,
                'sexo_paciente': sexo_paciente
            })
        conn.commit()
        print(f'Paciente {nome_paciente} adicionado com sucesso✅!')
    except oracledb.Error as e:
        print(f"Erro ao inserir paciente❗: {e}")
    finally:
        print("Fechando opção 1...")
        conn.close()
# Insere um novo paciente na tabela PACIENTES

def inserir_consulta(nome_consulta, descricao_consulta, dataHora_consulta, id_paciente):
    print('\n---------- Inserindo um novo consulta na tabela CONSULTAS -----------')
    conn = get_conexao()
    if not conn:
        return
    try:
        cursor = conn.cursor()
        sql = """
            INSERT INTO CONSULTAS (nome_consulta, descricao_consulta, dataHora_consulta, id_paciente)
            VALUES (:nome_consulta, :descricao_consulta, TO_DATE(:dataHora_consulta, 'dd/mm/yyyy hh24:mi'), :id_paciente)
            """
        cursor.execute(
            sql, {
                'nome_consulta': nome_consulta,
                'descricao_consulta': descricao_consulta,
                'dataHora_consulta': dataHora_consulta,
                'id_paciente': id_paciente
            })
        conn.commit()
        print(f'Consulta {nome_consulta} adicionado com sucesso✅!')
    except oracledb.Error as e:
        print(f"Erro ao inserir consulta❗: {e}")
    finally:
        print("Fechando opção...")
        conn.close()
# Insere uma nova consulta na tabela CONSULTAS

def inserir_exame(nome_exame, descricao_exame, dataHora_exame, id_paciente):
    print('\n---------- Inserindo um novo exame na tabela EXAMES -----------')
    conn = get_conexao()
    if not conn:
        return
    try:
        cursor = conn.cursor()
        sql = """
            INSERT INTO EXAMES (nome_exame, descricao_exame, dataHora_exame, id_paciente)
            VALUES (:nome_exame, :descricao_exame, TO_DATE(:dataHora_exame, 'dd/mm/yyyy hh24:mi'), :id_paciente)
            """
        cursor.execute(
            sql, {
                'nome_exame': nome_exame,
                'descricao_exame': descricao_exame,
                'dataHora_exame': dataHora_exame,
                'id_paciente': id_paciente
            })
        conn.commit()
        print(f'Exame {nome_exame} adicionado com sucesso✅!')
    except oracledb.Error as e:
        print(f"Erro ao inserir exame❗: {e}")
    finally:
        print("Fechando opção...")
        conn.close()
# Insere um novo exame na tabela EXAMES

# ------------------- LISTAGEM DE DADOS -------------------
def listar_pacientes():
    print('\n---------- Listando os pacientes da tabela PACIENTES -----------')
    conn = get_conexao()
    if not conn:
        return
    try:
        cursor = conn.cursor()
        sql = "SELECT * FROM PACIENTES"
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(f'ID: {row[0]} | Nome: {row[1]} | CPF: {row[2]} | Idade: {row[3]} | Sexo: {row[4]}')
    except oracledb.Error as e:
        print(f"Erro ao listar pacientes❗: {e}")
        print(f'Mensagem de erro: {e}')
    finally:
        print("Fechando a opção...")
        conn.close()
# Lista todos os pacientes cadastrados na tabela PACIENTES

def listar_consulta():
    print('\n-------------- Listando as consultas da tabela CONSULTAS --------------')
    conn = get_conexao()
    if not conn:
        return
    try:
        cursor = conn.cursor()
        sql = "SELECT * FROM CONSULTAS"
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(
                f'ID Consulta: {row[0]} | Nome Consulta: {row[1]} | Descrição Consulta: {row[2]} | DataHora Consulta: {row[3]} | ID Paciente: {row[4]}')
    except oracledb.Error as e:
        print(f"Erro ao listar Consultas❗: {e}")
        print(f'Mensagem de erro: {e}')
    finally:
        print("Fechando a opção...")
        conn.close()
# Lista todas as consultas cadastradas na tabela CONSULTAS

def listar_exames():
    print('\n-------------- Listando os exames da tabela EXAMES --------------')
    conn = get_conexao()
    if not conn:
        return
    try:
        cursor = conn.cursor()
        sql = "SELECT * FROM EXAMES"
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(
                f'ID Exame: {row[0]} | Nome Exame: {row[1]} | Descrição Exame: {row[2]} | DataHora Exame: {row[3]} | ID Paciente: {row[4]}')
    except oracledb.Error as e:
        print(f"Erro ao listar Exames❗: {e}")
        print(f'Mensagem de erro: {e}')
    finally:
        print("Fechando a opção...")
        conn.close()
# Lista todos os exames cadastrados na tabela EXAMES

# ------------------- BUSCA POR ID -------------------
def buscar_paciente_por_id(id_paciente):
    print('\n-------- Buscando um paciente na tabela PACIENTES pelo ID --------')
    conn = get_conexao()
    if not conn:
        return
    try:
        cursor = conn.cursor()
        sql = "SELECT * FROM PACIENTES WHERE id_paciente = :id_paciente"
        cursor.execute(sql, {'id_paciente': id_paciente})
        row = cursor.fetchone()
        if row:
            print(f'ID: {row[0]} | Nome: {row[1]} | CPF: {row[2]} | Idade: {row[3]} | Sexo: {row[4]}')
        else:
            print(f'Paciente com ID {id_paciente} não encontrado.')
    except oracledb.Error as e:
        print(f"Erro ao buscar paciente❗: {e}")
    finally:
        print("Fechando a opção ...")
        conn.close()
# Busca um paciente específico pelo ID na tabela PACIENTES

def buscar_consulta_por_id(id_consulta):
    print('\n----------- Buscando uma consulta na tabela CONSULTAS pelo ID ----------')
    conn = get_conexao()
    if not conn:
        return
    try:
        cursor = conn.cursor()
        sql = "SELECT * FROM CONSULTAS WHERE id_consulta = :id_consulta"
        cursor.execute(sql, {'id_consulta': id_consulta})
        row = cursor.fetchone()
        if row:
            print(
                f'ID Consulta: {row[0]} | Nome Consulta: {row[1]} | Descrição Consulta: {row[2]} | DataHora Consulta: {row[3]} | ID Paciente: {row[4]}')
        else:
            print(f'Consulta com ID {id_consulta} não encontrado.')
    except oracledb.Error as e:
        print(f"Erro ao buscar Consulta❗: {e}")
    finally:
        print("Fechando a opção ...")
        conn.close()
# Busca uma consulta específica pelo ID na tabela CONSULTAS

def buscar_exame_por_id(id_exame):
    print('\n----------- Buscando um exame na tabela EXAMES pelo ID ----------')
    conn = get_conexao()
    if not conn:
        return
    try:
        cursor = conn.cursor()
        sql = "SELECT * FROM EXAMES WHERE id_exame = :id_exame"
        cursor.execute(sql, {'id_exame': id_exame})
        row = cursor.fetchone()
        if row:
            print(
                f'ID Exame: {row[0]} | Nome Exame: {row[1]} | Descrição Exame: {row[2]} | DataHora Exame: {row[3]} | ID Paciente: {row[4]}')
        else:
            print(f'Exame com ID {id_exame} não encontrado.')
    except oracledb.Error as e:
        print(f"Erro ao buscar Exame❗: {e}")
    finally:
        print("Fechando a opção ...")
        conn.close()
# Busca um exame específico pelo ID na tabela EXAMES

# ------------------- ATUALIZAÇÃO DE DADOS -------------------
def atualizar_pacientes(id_paciente):
    conn = get_conexao()
    if not conn:
        return
    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT nome_paciente, cpf_paciente, idade_paciente, sexo_paciente
            FROM PACIENTES
            WHERE id_paciente = :id
        """, {'id': id_paciente})
        paciente = cursor.fetchone()
        if not paciente:
            print(f"Paciente com ID {id_paciente} não encontrado.")
            return
        nome_atual, cpf_atual, idade_atual, sexo_atual = paciente

        novo_nome = input(f"Nome atual: {nome_atual} | Novo nome: ") or nome_atual
        novo_cpf = input(f"CPF atual: {cpf_atual} | Novo CPF: ") or cpf_atual
        nova_idade = input(f"Idade atual: {idade_atual} | Nova idade: ") or idade_atual
        novo_sexo = input(f"Sexo atual: {sexo_atual} | Novo sexo: ") or sexo_atual

        cursor.execute("""
            UPDATE PACIENTES
            SET nome_paciente = :nome,
                cpf_paciente = :cpf,
                idade_paciente = :idade,
                sexo_paciente = :sexo
            WHERE id_paciente = :id
        """, {
            'id': id_paciente,
            'nome': novo_nome,
            'cpf': novo_cpf,
            'idade': int(nova_idade),
            'sexo': novo_sexo
        })
        conn.commit()
        print(f"\nPaciente {novo_nome} atualizado com sucesso✅!")
    except oracledb.Error as e:
        print(f"Erro ao atualizar paciente❗: {e}")
    finally:
        conn.close()
# Atualiza os dados de um paciente existente na tabela PACIENTES

def atualizar_consultas(id_consulta):
    conn = get_conexao()
    if not conn:
        return
    try:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT nome_consulta, descricao_consulta, TO_CHAR(dataHora_consulta, 'dd/mm/yyyy hh24:mi' ) "
            "FROM CONSULTAS WHERE id_consulta = :id", {'id': id_consulta}
        )
        consulta = cursor.fetchone()
        if not consulta:
            print(f"Consulta com ID {id_consulta} não encontrada.")
            return
        nome_atual, descricao_atual, dataHora_atual = consulta
    except oracledb.Error as e:
        print(f"Erro ao buscar consulta❗: {e}")
        return
    finally:
        conn.close()

    print("\nDeixe o campo vazio se não quiser alterar o atributo.")

    novo_nome = input(f"\nNome atual: {nome_atual} | Novo nome: ") or nome_atual
    nova_descricao = input(f"Descrição atual: {descricao_atual} | Nova descrição: ") or descricao_atual
    nova_dataHora = input(f"DataHora atual: {dataHora_atual} | Nova dataHora (dd/mm/yyyy hh24:mi): ") or dataHora_atual

    conn = get_conexao()
    try:
        cursor = conn.cursor()
        sql = """
            UPDATE CONSULTAS
            SET nome_consulta = :nome,
                descricao_consulta = :descricao,
                dataHora_consulta = TO_DATE(:dataHora, 'dd/mm/yyyy hh24:mi' )
            WHERE id_consulta = :id
        """
        cursor.execute(sql, {
            'id': id_consulta,
            'nome': novo_nome,
            'descricao': nova_descricao,
            'dataHora': nova_dataHora
        })
        conn.commit()
        print(f"\nConsulta {novo_nome} atualizada com sucesso✅!")
    except oracledb.Error as e:
        print(f"Erro ao atualizar consulta❗: {e}")
    finally:
        conn.close()
# Atualiza os dados de uma consulta existente na tabela CONSULTAS

def atualizar_exames(id_exame):
    conn = get_conexao()
    if not conn:
        return
    try:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT nome_exame, descricao_exame, TO_CHAR(dataHora_exame, 'dd/mm/yyyy hh24:mi') "
            "FROM EXAMES WHERE id_exame = :id", {'id': id_exame}
        )
        exame = cursor.fetchone()
        if not exame:
            print(f"Exame com ID {id_exame} não encontrado.")
            return
        nome_atual, descricao_atual, dataHora_atual = exame
    except oracledb.Error as e:
        print(f"Erro ao buscar exame❗: {e}")
        return
    finally:
        conn.close()

    novo_nome = input(f"Nome atual: {nome_atual} | Novo nome: ") or nome_atual
    nova_descricao = input(f"Descrição atual: {descricao_atual} | Nova descrição: ") or descricao_atual
    nova_data = input(f"DataHora atual: {dataHora_atual} | Nova dataHora (dd/mm/yyyy hh24:mi): ") or dataHora_atual

    conn = get_conexao()
    try:
        cursor = conn.cursor()
        sql = """
            UPDATE EXAMES
            SET nome_exame = :nome,
            descricao_exame = :descricao,
            dataHora_exame = TO_DATE(:dataHora, 'dd/mm/yyyy hh24:mi' )
            WHERE id_exame = :id
        """
        cursor.execute(sql, {
            'id': id_exame,
            'nome': novo_nome,
            'descricao': nova_descricao,
            'dataHora': nova_data
        })
        conn.commit()
        print(f"\nExame {novo_nome} atualizado com sucesso✅!")
    except oracledb.Error as e:
        print(f"Erro ao atualizar exame❗: {e}")
    finally:
        conn.close()
# Atualiza os dados de um exame existente na tabela EXAMES

# ------------------- DELEÇÃO DE DADOS -------------------
def deletar_pacientes(id_paciente):
    print('\n------------ Deletando um paciente na tabela PACIENTES ---------------')
    conn = get_conexao()
    if not conn:
        return
    try:
        cursor = conn.cursor()
        sql = "DELETE FROM PACIENTES WHERE id_paciente = :id_paciente"
        cursor.execute(sql, {'id_paciente': id_paciente})
        conn.commit()
        print(f'Paciente com ID {id_paciente} deletado com sucesso✅!')
    except oracledb.Error as e:
        print(f"Erro ao deletar paciente❗: {e}")
    finally:
        print("Fechando a opção ...")
        conn.close()
# Remove um paciente da tabela PACIENTES

def deletar_consulta(id_consulta):
    print('\n----------------- Deletando uma consulta na tabela CONSULTAS ----------------')
    conn = get_conexao()
    if not conn:
        return
    try:
        cursor = conn.cursor()
        sql = "DELETE FROM CONSULTAS WHERE id_consulta = :id_consulta"
        cursor.execute(sql, {'id_consulta': id_consulta})
        conn.commit()
        print(f'Consulta com ID {id_consulta} deletada com sucesso✅!')
    except oracledb.Error as e:
        print(f"Erro ao deletar consulta❗: {e}")
    finally:
        print("Fechando a opção ...")
        conn.close()
# Remove uma consulta da tabela CONSULTAS

def deletar_exame(id_exame):
    print('\n----------------- Deletando um exame na tabela EXAMES ----------------')
    conn = get_conexao()
    if not conn:
        return
    try:
        cursor = conn.cursor()
        sql = "DELETE FROM EXAMES WHERE id_exame = :id_exame"
        cursor.execute(sql, {'id_exame': id_exame})
        conn.commit()
        print(f'Exame com ID {id_exame} deletado com sucesso✅!')
    except oracledb.Error as e:
        print(f"Erro ao deletar exame❗: {e}")
    finally:
        print("Fechando a opção ...")
        conn.close()
# Remove um exame da tabela EXAMES

# ------------------- MENU INTERATIVO -------------------
def main():
    while True:
        print("\n==================================================================================")
        print("👨‍⚕️----------------------------- MENU PRINCIPAL --------------------------------🩺")
        print("==================================================================================")
        print("-----Menu de opções para gerenciar o banco de dados de um consultório médico.-----")
        print("\nEscolha a tabela que deseja editar:")
        print("\n[1]. TABELA DE PACIENTES")
        print("\n[2]. TABELA DE CONSULTAS")
        print("\n[3]. TABELA DE EXAMES")
        print("\n[0]. Sair")
        try:
            escolha = int(input("\nEscolha uma opção: "))
            if escolha not in [0, 1, 2, 3, 4, 5]:
                print("\nOpção inválida! Por favor, escolha uma opção entre 0 e 5.")
                continue
        except ValueError:
            print("\nErro: Por favor, digite um número válido!")
            continue
        if escolha == 1:
            menu_pacientes()
        elif escolha == 2:
            menu_consultas()
        elif escolha == 3:
            menu_exames()
        elif escolha == 0:
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")


def menu_pacientes():
    while True:
        print("\n-------------------------------- PACIENTES -------------------------------------")
        print("\n[1]. Inserir paciente")
        print("[2]. Listar pacientes")
        print("[3]. Buscar paciente por ID")
        print("[4]. Atualizar paciente")
        print("[5]. Deletar paciente")
        print("[0]. Voltar")
        try:
            escolha = int(input("\nEscolha uma opção: "))
            if escolha not in [0, 1, 2, 3, 4, 5]:
                print("\nOpção inválida! Por favor, escolha uma opção entre 0 e 5.")
                continue
        except ValueError:
            print("\nErro: Por favor, digite um número válido!")
            continue
        if escolha == 1:
            try:
                nome = str(input("Nome do paciente: "))
                cpf = input("CPF siga este exemplo: (000-000-000-00) : ")
                idade = int(input("Idade: "))
                sexo = input("Sexo: ")
                inserir_paciente(nome, cpf, idade, sexo)
            except ValueError:
                print("\nAs informações de Usuário são Inválidas! \nPor favor Siga o padrão!")
        elif escolha == 2:
            try:
                listar_pacientes()
            except ValueError:
                print("⚠️ Por favor insira um número valido.")
        elif escolha == 3:
            try:
                id_paciente = int(input("ID do paciente: "))
                buscar_paciente_por_id(id_paciente)
            except ValueError:
                print("⚠️ Por favor, insira um número válido para o ID do paciente.")
        elif escolha == 4:
            try:
                id_paciente = int(input("ID do paciente: "))
                print("\nPara as opções que NAO deseja atualizar, deixe o campo vazio.")
                atualizar_pacientes(id_paciente)
            except ValueError:
                print("\n⚠️ Por favor, insira um número válido para o ID do paciente")
        elif escolha == 5:
            try:
                id_paciente = int(input("ID do paciente: "))
                deletar_pacientes(id_paciente)
            except ValueError:
                print("\n⚠️ Por favor, insira um número válido para o ID do paciente")
        elif escolha == 0:
            break
        else:
            print("Opção inválida.")
# Submenu para gerenciar PACIENTES (inserir, listar, buscar, atualizar, deletar)

def menu_consultas():
    while True:
        print("\n------------------------------ CONSULTAS ------------------------------------")
        print("\n[1]. Inserir consulta")
        print("[2]. Listar consultas")
        print("[3]. Buscar consulta por ID")
        print("[4]. Atualizar consulta")
        print("[5]. Deletar consulta")
        print("[0]. Voltar")
        try:
            escolha = int(input("\nEscolha uma opção: "))
            if escolha not in [0, 1, 2, 3, 4, 5]:
                print("\nOpção inválida! Por favor, escolha uma opção entre 0 e 5.")
                continue
        except ValueError:
            print("\nErro: Por favor, digite um número válido!")
            continue

        if escolha == 1:
            try:
                nome = input("Nome da consulta: ")
                descricao = input("Descrição: ")
                dataHora = input("Data (dd/mm/aaaa hh24:mi): ")
                id_paciente = int(input("ID do paciente: "))
                inserir_consulta(nome, descricao, dataHora, id_paciente)
            except ValueError:
                print("\nAs informações de Usuário são Inválidas! \nPor favor Siga o padrão!")

        elif escolha == 2:
            listar_consulta()
        elif escolha == 3:
            try:
                id_cons = int(input("ID da consulta: "))
                buscar_consulta_por_id(id_cons)
            except ValueError:
                print("\nDigite apenas números")
        elif escolha == 4:
            try:
                id_cons = int(input("ID da consulta: "))
                atualizar_consultas(id_cons)
            except ValueError:
               print("\nDigite apenas números")
        elif escolha == 5:
            try:
                id_cons = int(input("ID da consulta: "))
                deletar_consulta(id_cons)
            except ValueError:
                print("\nDigite apenas números")
        elif escolha == 0:
            break
        else:
            print("Opção inválida.")
# Submenu para gerenciar CONSULTAS (inserir, listar, buscar, atualizar, deletar)

def menu_exames():
    while True:
        print("\n-------------------------------- EXAMES -------------------------------------")
        print("\n[1]. Inserir exame")
        print("[2]. Listar exames")
        print("[3]. Buscar exame por ID")
        print("[4]. Atualizar exame")
        print("[5]. Deletar exame")
        print("[0]. Voltar")

        try:
            escolha = int(input("\nEscolha uma opção: "))
            if escolha not in [0, 1, 2, 3, 4, 5]:
                print("\nOpção inválida! Por favor, escolha uma opção entre 0 e 5.")
                continue
        except ValueError:
            print("\nErro: Por favor, digite um número válido!")
            continue

        if escolha == 1:
            try:
                nome = input("Nome do exame: ")
                descricao = input("Descrição: ")
                dataHora = input("Data (dd/mm/aaaa hh24:mi): ")
                id_paciente = int(input("ID do paciente: "))
                inserir_exame(nome, descricao, dataHora, id_paciente)
            except ValueError:
                print("\nAs informações de Usuário são Inválidas! \nPor favor Siga o padrão!")
        elif escolha == 2:
            listar_exames()
        elif escolha == 3:
            try:
                id_exame = int(input("ID do exame: "))
                buscar_exame_por_id(id_exame)
            except ValueError:
                print("\nErro: Digite apenas numeros")
        elif escolha == 4:
            id_exame = int(input("ID do exame: "))
            print("\nPara as opções que NAO deseja atualizar, deixe o campo vazio.")
            atualizar_exames(id_exame)
        elif escolha == 5:
            try:
                id_exame = int(input("ID do exame: "))
                deletar_exame(id_exame)
            except ValueError:
                print("\nErro: Digite apenas numeros")
        elif escolha == 0:
            break
        else:
            print("Opção inválida.")
# Submenu para gerenciar EXAMES (inserir, listar, buscar, atualizar, deletar)

main()