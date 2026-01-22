from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, world! cambiooOoOoO"

@app.route("/hola")
def hola():
    return "Hola mundo!"

@app.route("/user/<string:user>")
def user(user):
    return f"Hola ,{user}"

@app.route("/user/<int:id>/<string:user>")
def username(id,user):
    return f"<h1>Hola ,{user}!, Tu ID es: {id}"

@app.route("/user/<float:n1>/<float:n2>")
def suma(n1,n2):
    return f"<h1>La suma es,{n1+n2}</h1>"

@app.route("/default/")
@app.route("/default/<string:param>")
def func(param=" Usuario predeterminado"):
    return f"<h1>Hola, {param}</h1>"

@app.route("/operas")
def operas():
    return '''
    <form>
    <label for="name">Name:</label>
    <input type="text" id="name" name="name" required>
    </br>
    <label for="name">apaterno:</label>
    <input type="text" id="name" name="name" required>
</form>
    '''

if __name__ == "__main__":
    app.run(debug=True)