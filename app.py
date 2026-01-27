from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    titulo="Flask IDGS801"
    lista = ["Juan","Mario","Pedro","Dario"]
    return render_template("index.html",titulo=titulo,lista=lista)

@app.route("/operasBas", methods=["GET","POST"])
def operasBas():
    n1=0
    n2=0
    res=0
    if request.method=='POST':
        n1=request.form.get('n1')
        n2=request.form.get('n2')
        res=float(n1)+float(n2)
    return render_template("operasBas.html",n1=n1,n2=n2,res=res)

@app.route("/resultado", methods=["GET","POST"])
def resultado():
    n1=request.form.get('n1')
    n2=request.form.get('n2')
    tem=float(n1)+float(n2)
    return f"La suma es: {tem}"
    

@app.route("/alumnos")
def alumnos():
    return render_template("alumnos.html")

@app.route("/usuarios")
def usuarios():
    return render_template("usuarios.html")


if __name__ == "__main__":
    app.run(debug=True)