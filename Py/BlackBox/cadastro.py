import mysql.connector
from getpass import getpass

# Conexão com o banco de dados
cnx = mysql.connector.connect(
    user='root',
    host='127.0.0.1',
    database='Restaurante'
)

# Função para cadastrar um novo usuário
def cadastrar_usuario():
    cpf = input("Digite o CPF: ")
    nome = input("Digite o nome: ")
    idade = input("Digite a idade: ")
    endereco = input("Digite o endereço: ")
    email = input("Digite o email: ")
    telefone = input("Digite o telefone: ")
    senha = getpass("Digite a senha: ")

    # Verificar se o CPF já existe no banco de dados
    cursor = cnx.cursor()
    query = "SELECT * FROM Clientes WHERE CPF = %s"
    cursor.execute(query, (cpf,))
    if cursor.fetchone():
        print("CPF já existe no banco de dados!")
        return

    # Inserir o novo usuário no banco de dados
    query = "INSERT INTO Clientes (CPF, Nome, Idade, Endereco, Email, Telefone, Senha) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (cpf, nome, idade, endereco, email, telefone, senha))
    cnx.commit()
    print("Usuário cadastrado com sucesso!")

# Função para fazer login
def fazer_login():
    email = input("Digite o email: ")
    senha = getpass("Digite a senha: ")

    # Verificar se o email e senha estão corretos
    cursor = cnx.cursor()
    query = "SELECT * FROM Clientes WHERE Email = %s AND Senha = %s"
    cursor.execute(query, (email, senha))
    if cursor.fetchone():
        print("Login efetuado com sucesso!")
    else:
        print("Email ou senha incorretos!")

# Menu principal
while True:
    print("1. Cadastrar usuário")
    print("2. Fazer login")
    print("3. Sair")
    opcao = input("Digite a opção: ")
    if opcao == "1":
        cadastrar_usuario()
    elif opcao == "2":
        fazer_login()
    elif opcao == "3":
        break
    else:
        print("Opção inválida!")    