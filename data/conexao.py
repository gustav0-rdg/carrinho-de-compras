import mysql.connector
class Conexao:
    # Criando conexao
    def criar_conexao():
        conexao = mysql.connector.connect(
            host="127.0.0.1",
            port=3306,
            user="root",
            password="root",
            database = "dbcarrinho"
        )

        return conexao