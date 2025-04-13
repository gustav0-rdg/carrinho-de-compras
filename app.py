from flask import render_template, Flask, session, request, redirect
from model.controller_usuario import Usuario
from model.controller_produtos import Produtos
app = Flask(__name__)

app.secret_key = "12345678amoaliicai"

@app.route("/")
def pag_inicial():
    return render_template("login.html")

@app.route("/logar", methods=["POST"])
def logar():
    usuario = request.form.get("usuario")
    senha = request.form.get("senha")
    logou = Usuario.logar(usuario, senha)
    
    if logou:
        if senha == "admin123" and usuario == "admin123" :
            return redirect("/cadastro/produtos")
        else:
            return redirect("/catalogo")
    else:
        return redirect("/")

@app.route("/cadastro")
def pag_cadastrar():
    return render_template("cadastro.html")

@app.route("/cadastrar/usuario", methods=["POST"])
def cadastrar():
    usuario = request.form.get('usuario')
    nome = request.form.get('nome')
    senha = request.form.get('senha')
    Usuario.cadastrar(usuario, nome, senha)
    return redirect("/")

@app.route("/catalogo")
def pag_catalogo():
    if 'usuario' in session:
        produtos = Produtos.exibir()
        print(produtos)
        return render_template("compras.html", produtos = produtos)
    else:
        return redirect("/")

@app.route("/cadastro/produtos", methods=["GET"])
def pag_cadastro_prod():
    if 'usuario' in session:
        return render_template("cadastro-produto.html")
    else:
        return redirect("/")
    
@app.route("/cadastrar/produtos/cadastro", methods=["POST"])
def cadastrar_produtos():
    nome = request.form.get("nome")
    descricao = request.form.get("descricao")
    preco = request.form.get("preco")
    categoria = request.form.get("categoria")
    Produtos.cadastrar(nome, descricao, preco, categoria)
    return redirect("/")

app.run(debug=True)