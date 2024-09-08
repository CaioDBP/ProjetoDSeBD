import mysql.connector
from datetime import datetime
from tabulate import tabulate

# Configurações do banco de dados
host = '127.0.0.1'
database = 'Restaurante'
user = 'root'

# Conectar ao banco de dados
cnx = mysql.connector.connect(
    host=host,
    database=database,
    user=user,
)

# Criar um cursor
cursor = cnx.cursor()

def cadastrar_cliente():
    print("Cadastro de Cliente")
    print("--------------------")

    # Solicitar os dados do usuário
    cpf = input("Digite o CPF: ")
    nome = input("Digite o nome: ")
    senha = input("Digite a senha: ")
    sexo = input("Digite o sexo: ")
    idade = input("Digite a idade: ")
    endereco = input("Digite o endereço: ")
    email = input("Digite o email: ")
    telefone = input("Digite o telefone: ")

    # Criar a query de inserção
    query = """
        INSERT INTO Clientes (
            CPF,
            Nome,
            Senha,
            Sexo,
            Idade,
            Endereco,
            Email,
            Telefone,
            Data_cadastro
        ) VALUES (
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s
        )
    """

    # Obter a data de cadastro atual
    data_cadastro = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Executar a query
    cursor.execute(query, (
        cpf,
        nome,
        senha,
        sexo,
        idade,
        endereco,
        email,
        telefone,
        data_cadastro
    ))

    # Commitar as alterações
    cnx.commit()

    # Obter o ID do cliente cadastrado
    cursor.execute("SELECT LAST_INSERT_ID()")
    id_cliente = cursor.fetchone()[0]

    # Obter o ID da filial (você pode substituir por uma lógica para obter o ID da filial)
    id_filial = 1

    # Atualizar o cliente com o ID da filial
    query = "UPDATE Clientes SET ID_filial = %s WHERE ID_cliente = %s"
    cursor.execute(query, (id_filial, id_cliente))

    # Commitar as alterações
    cnx.commit()

    # Obter os dados do cliente cadastrado
    cursor.execute("SELECT * FROM Clientes WHERE ID_cliente = %s", (id_cliente,))
    cliente = cursor.fetchone()

    # Imprimir os dados do cliente cadastrado
    print("Cliente cadastrado com sucesso!")

    # Imprimir a tabela com o novo usuário cadastrado
    print("\nTabela de Clientes:")
    cursor.execute("SELECT * FROM Clientes")
    clientes = cursor.fetchall()
    headers = ["ID", "ID Filial", "CPF", "Nome", "Senha", "Sexo", "Idade", "Endereço", "Email", "Telefone", "Data de Cadastro"]
    print(tabulate(clientes, headers, tablefmt="grid"))

def main():
    while True:
        print("Menu")
        print("-----")
        print("1. Cadastrar cliente")
        print("2. Sair")
        opcao = input("Digite a opção: ")

        if opcao == "1":
            cadastrar_cliente()
        elif opcao == "2":
            break
        else:
            print("Opção inválida. Tente novamente.")

    # Fechar o cursor e a conexão
    cursor.close()
    cnx.close()

if __name__ == "__main__":
    main()