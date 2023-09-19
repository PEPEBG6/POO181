from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_mysqldb import MySQL
#from flask_session import Session
from datetime import datetime
#from reportlab.lib.pagesizes import letter
#from reportlab.pdfgen import canvas
#from reportlab.lib import colors
#from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
#from reportlab.platypus import SimpleDocTemplate, Paragraph

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


@app.route('/ingresar', methods=['POST'])
def ingresar():
    if request.method == 'POST':
        Vrfc = request.form['rfc']
        pas = request.form['contraseña']
        
        Clog = mysql.connection.cursor()
        Clog.execute('select id from medicos where rfc=%s and contraseña =%s', (Vrfc, pas))
        id_usuario = Clog.fetchone()
        
        if id_usuario:
            session['rfc'] = id_usuario  # Establecer variable de sesión
            return render_template('index.html')
        else:
            flash('No se encontró el usuario o contraseña')
            return render_template('login.html')
        

if __name__ == '__main__':
    app.run(port=2000, debug=True)