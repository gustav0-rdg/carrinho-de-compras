from flask import render_template, Flask, session, request, redirect

app = Flask(__name__)

app.secret_key = "12345678amoaliicai"

@app.route("/")
def pag_inicial():
    return render_template("login.html")

app.run(debug=True)