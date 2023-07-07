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

@app.route('/registros.html')
def registros():
    return render_template('registros.html')

@app.route('/registro',methods=['POST'])
def registro():

    if request.method == 'POST':

        Vusuario=request.form['usuario']
        Vnombre=request.form['Nombre']
        VapellidoP=request.form['ApellidoP']
        VapellidoM=request.form['ApellidoM']
        Vrol=request.form['Rol']
        Vcontraseña=request.form['Contraseña']

        cs= mysql.connection.cursor()
        cs.execute('insert into usuarios (usuario,nombre,apellido_paterno,apellido_materno,id_rol,contraseña) values(%s,%s,%s,%s,%s,%s)',(Vusuario,Vnombre,VapellidoP,VapellidoM,Vrol,Vcontraseña))
        mysql.connection.commit()

    flash('Registro realizado con exito')
    return redirect(url_for('registros'))


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


@app.route('/cursos.html')
def cursos():
    return render_template('cursos.html')

@app.route('/curso',methods=['POST'])
def curso():

    if request.method == 'POST':

        Vnombre=request.form['Nombre']
        Vmateria=request.form['Materia']
        Vtema=request.form['Tema']
        Vdescrpcion=request.form['Descripcion']
        Vhorario=request.form['Horario']
        Vlocalizacion=request.form['Localizacion']

        cs= mysql.connection.cursor()
        cs.execute('insert into cursos (nombre,materia,tema,descripcion,horario,id_localizacion) values(%s,%s,%s,%s,%s,%s)',(Vnombre,Vmateria,Vtema,Vdescrpcion,Vhorario,Vlocalizacion))
        mysql.connection.commit()


    flash('Curso publicado con exito')
    return redirect(url_for('cursos'))


@app.route('/perfil')
def perfil():
    return render_template('perfil.html')


@app.route('/historial')
def historial():
    return render_template('historial.html')


# -------------------------------------------------------

if __name__ == '__main__':
    app.run(port=1000, debug=True)