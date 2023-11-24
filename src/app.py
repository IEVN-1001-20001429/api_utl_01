from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    titulo = 'IEVN-1001'
    list = ["Juan", "Pedro", "Carlos"]
    return render_template('index.html', titulo=titulo, list = list)

@app.route('/uno')
def uno():
    return render_template('uno.html')

@app.route('/dos')
def dos():
    return render_template('dos.html')

@app.route('/user/<string:user>')
def user(user):
    return 'El usuario es: {}'.format(user)

@app.route('/number/<int:n1>')
def number(n1):
    return 'El numero es: {}'.format(n1)

@app.route('/datos/<string:nom>/<int:id>')
def datos(nom,id):
    return '<h1>ID: {} -  Nombre: {}</h1>'.format(nom,id)

@app.route('/suma/<float:num1>/<float:num2>')
def suma(num1,num2):
    return '<h1>La suma es: {}</h1>'.format(num1+num2)

@app.route('/default')
@app.route('/default/<string:nom>')
def nom(nom='Dario'):
    return '<h1>El nombre es: {}</h1>'.format(nom)


if __name__ == "__main__":
    app.run(debug=True)