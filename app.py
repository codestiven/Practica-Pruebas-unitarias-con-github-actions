from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return '¡Hola, mundo!'

@app.route('/saludo/<nombre>')
def saludo(nombre):
    return f'¡Hola, {nombre}!'

@app.route('/template')
def template():
    return render_template('template.html', message='¡Hola desde la plantdilla!!')

if __name__ == '__main__':
    app.run(debug=True)
