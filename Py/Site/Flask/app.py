from flask import Flask, request, jsonify
import mysql.connector
from datetime import datetime
from tabulate import tabulate

app = Flask(__name__)

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

@app.route('/cadastrar_cliente', methods=['POST'])
def cadastrar_cliente():
    dados = request.get_json()
    cpf = dados['cpf']
    nome = dados['nome']
    senha = dados['senha']
    sexo = dados['sexo']
    idade = dados['idade']
    endereco = dados['endereco']
    email = dados['email']
    telefone = dados['telefone']

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

    # Retornar mensagem de sucesso
    return jsonify({'mensagem': 'Cliente cadastrado com sucesso!'})

@app.route('/login_cliente', methods=['POST'])
def login_cliente():
    dados = request.get_json()
    email = dados['email']
    senha = dados['senha']

    # Criar a query de seleção
    query = "SELECT * FROM Clientes WHERE Email = %s AND Senha = %s"
    cursor.execute(query, (email, senha))

    # Obter os dados do cliente
    cliente = cursor.fetchone()

    if cliente:
        # Retornar mensagem de sucesso
        return jsonify({'mensagem': 'Login realizado com sucesso!'})
    else:
        # Retornar mensagem de erro
        return jsonify({'mensagem': 'CPF ou senha inválidos. Tente novamente.'}), 401

@app.route('/clientes', methods=['GET'])
def get_clientes():
    # Obter os dados dos clientes
    cursor.execute("SELECT * FROM Clientes")
    clientes = cursor.fetchall()
    headers = ["ID", "ID Filial", "CPF", "Nome", "Senha", "Sexo", "Idade", "Endereço", "Email", "Telefone", "Data de Cadastro"]
    tabela = tabulate(clientes, headers, tablefmt="grid")
    return jsonify({'tabela': tabela})

if __name__ == '__main__':
    app.run(debug=True)