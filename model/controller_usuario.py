import mysql.connector
from hashlib import sha256
from data.conexao import Conexao
from flask import session

class Usuario:
    def cadastrar(usuario, nome, senha):
        senha = sha256(str(senha).encode()).hexdigest()
        try:
            conexao = Conexao.criar_conexao()
            cursor = conexao.cursor()

            sql = "INSERT INTO tbusuarios(usuario, nome, senha) VALUES(%s, %s, %s)"
            valores = (usuario, nome, senha)
            cursor.execute(sql, valores)
            conexao.commit()

        except Exception as e:
            print(f'O erro é {e}')
        finally: 
            #  Se a variavel conexao existir, ela será fechada
            if 'conexao' in locals():
                conexao.close()

    def logar(usuario, senha):  
        senha = sha256(str(senha).encode()).hexdigest()
        try:
            conexao = Conexao.criar_conexao()
            cursor = conexao.cursor(dictionary=True)
            sql = "SELECT * FROM tbusuarios WHERE usuario = %s AND BINARY senha = %s"
            valores = (usuario, senha)
            cursor.execute(sql, valores)
            resultado = cursor.fetchone()

            if resultado: 
                session['usuario'] = resultado['usuario']
                session['nome'] = resultado['nome']
                return True
            else:
                return False
        except Exception as e:
            print(f'Erro: {e}')
        finally:
            conexao.close()