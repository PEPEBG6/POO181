from flask import Flask, request, session, render_template, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__, static_folder='public', template_folder='templates')
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "yourSpace"
app.secret_key = 'mysecretkey'
mysql = MySQL(app)

# -------------------------------------------------------


@app.route('/')
def login():
    return render_template('login.html')


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/registros')
def registros():
    return render_template('registros.html')


@app.route('/ingresar', methods=['POST'])
def ingresar():
    if request.method == 'POST':
        Vusername = request.form['username']
        Vpassword = request.form['password']

    usu = {
        'diego_d': '1234',
        'pato_m': '4321'
    }

    if Vusername == 'diego_d':
        if Vusername in usu and usu[Vusername] == Vpassword:
            session['username'] = Vusername
            return redirect(url_for('index'))
        else:
            flash('Usuario o contraseña incorrectos')
            return redirect(url_for('login'))
    elif Vusername == 'pato_m':
        if Vusername in usu and usu[Vusername] == Vpassword:
            session['username'] = Vusername
            return redirect(url_for('index'))
        else:
            flash('Usuario o contraseña incorrectos')
            return redirect(url_for('login'))
    else:
        flash('Usuario o contraseña incorrectos')
        return redirect(url_for('login'))


@app.route('/cursos')
def cursos():
    return render_template('cursos.html')


@app.route('/perfil')
def perfil():
    return render_template('perfil.html')


@app.route('/historial')
def historial():
    return render_template('historial.html')


# -------------------------------------------------------

if __name__ == '__main__':
    app.run(port=1000, debug=True)