from flask import Flask, request, session, render_template, redirect, url_for, flash
#from flask_session import Session
from flask_mysqldb import MySQL
from datetime import datetime

app = Flask(__name__, static_folder='static', template_folder='templates')
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "medicos"
app.config['SECRET_KEY'] = 'mysecretkey'
app.config['SESSION_TYPE'] = 'filesystem'

mysql = MySQL(app)
#Session(app)


@app.route('/')
def login():
    return render_template('login.html')


@app.route('/comprobar', methods=['POST'])
def comprobar():
    if request.method == 'POST':
        usuario = request.form['rfc']
        contraseña = request.form['contraseña']

        Clog = mysql.connection.cursor()
        Clog.execute('select id from usuarios where usuario=%s and contraseña =%s', (usuario, contraseña))
        id_usuario = Clog.fetchone()

        if id_usuario:
            session['usuario'] = usuario  # Establecer variable de sesión
            return redirect(url_for('index'))
        else:
            flash('No se encontró el usuario o contraseña')
            return redirect(url_for('login'))
        

if __name__ == '__main__':
    app.run(port=2000, debug=True)