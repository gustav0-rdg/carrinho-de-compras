from flask import render_template, Flask, session, request, redirect
from model.controller_usuario import Usuario
app = Flask(__name__)

app.secret_key = "12345678amoaliicai"

@app.route("/")
def pag_inicial():
    return render_template("login.html")

@app.route("/logar", methods=["POST"])
def logar():
    usuario = request.form.get("usuario")
    senha = request.form.get("usuario")
    logou = Usuario.logar(usuario, senha)
    if logou:
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
    return render_template("compras.html")

app.run(debug=True)