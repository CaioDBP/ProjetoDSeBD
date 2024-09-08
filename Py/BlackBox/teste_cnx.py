import mysql.connector

cnx = mysql.connector.connect(
    user='root',
    host='127.0.0.1',
    database='Restaurante'
)

print(cnx.is_connected())  # Imprime True se a conexão foi estabelecida com sucesso

# Fechar a conexão quando terminar
cnx.close()