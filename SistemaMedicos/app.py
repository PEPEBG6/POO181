#importacion del framework
from flask import Flask, request, session, render_template, redirect, url_for, flash
from flask_mysqldb import MySQL


#Inicializacion del APP
app = Flask(__name__, static_folder='public', template_folder='templates')
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='SistemasMedicos'
app.secret_key= 'mysecrety'
mysql= MySQL(app)

#Declaracion de ruta http://localhost:5000
@app.route('/')
def bienvenida():
  
  return render_template('bienvenida.html')





#Ejecucion del servidor en el puerto 5000
if __name__ == '__main__':
  app.run(port=1000,debug=True)
