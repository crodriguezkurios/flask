from flask import Flask, render_template
app = Flask(__name__)

frutas = ['manzana', 'pera', 'naranja', 'uva', 'mango']

@app.route("/<string:name>")
def index(name):
    return render_template('index.jinja', message=f'hola {name}', numbers=frutas)


@app.route("/fruta/<int:id>")
def fruta(id):

    try: 
        index = id - 1
        return frutas[index]

    except IndexError:
    
        return 'no hay fruta'


@app.route("/home")
def home():
    return "hello world" + str(58*966)

@app.route("/libros/<int:id>")
def libros(id):
    return str(id)


if __name__ == '__main__':
    app.run(debug=True)