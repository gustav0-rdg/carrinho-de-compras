import mysql.connector
from data.conexao import Conexao

class Produtos:
    def cadastrar(nome, descricao, valor, categoria):
        try:
            conexao = Conexao.criar_conexao()
            cursor = conexao.cursor()

            sql = "INSERT INTO tbprodutos(nome, descricao, preco, categoria) VALUES(%s, %s, %s, %s);"

            valores = (nome, descricao, valor, categoria)
            cursor.execute(sql, valores)
            conexao.commit()
        except Exception as e:
            print(f"O erro é: {e}")
        finally:
            if 'conexao' in locals():
                conexao.close()
    
    def exibir():
        try:
            conexao = Conexao.criar_conexao()
            cursor = conexao.cursor(dictionary=True)

            sql = "SELECT * FROM tbprodutos;"

            cursor.execute(sql)
            resultado = cursor.fetchall()
            return resultado
        
        except Exception as e:
            print(f"Erro: {e}")

        finally: 
            conexao.close()