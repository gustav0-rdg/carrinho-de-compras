import mysql.connector
from hashlib import sha256
from data.conexao import Conexao

class Usuario:
    def cadastrar(usuario, nome, senha):
        senha = sha256(str(senha).encode()).hexdigest()
        try:
            conexao = Conexao.criar_conexao()
            cursor = conexao.cursor()

            sql = "INSERT INTO tbusuarios(usuario, nome, senha) VALUES(%s, %s, %s)"
            valores = (usuario, nome, senha)
            cursor.execute(sql, valores)
            cursor.commit()

        except Exception as e:
            print(f'O erro é {e}')
        finally: 
            #  Se a variavel conexao existir, ela será fechada
            if 'conexao' in locals():
                conexao.close()