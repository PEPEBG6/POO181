#importacion del framework
from flask import Flask, render_template, request
from flask_mysqldb import MySQL

#Inicializacion del APP
app= Flask (__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='dbflask'
mysql= MySQL(app)

#Declaracion de ruta http://localhost:5000
@app.route('/')
def index():
  
  return render_template('index.html')

#rura http:localhost:5000/guardar tipo POST para insert
@app.route('/guardar',methods=['POST'])
def guardar():
  if request.method == 'POST':
    titulo=request.form['txtTitulo']
    artista=request.form['txtArtista']
    anio=request.form['txtAnio']
    print(titulo,artista,anio)

  return "Los datos llegaron Amigo ;)"

@app.route('/eliminar')
def eliminar():
  
  return "Se elimino en la BD"

#Ejecucion del servidor en el puerto 5000
if __name__ == '__main__':
  app.run(port=5000,debug=True)

