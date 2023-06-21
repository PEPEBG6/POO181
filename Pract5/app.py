#importacion del framework
from flask import Flask, render_template, request,redirect,url_for,flash
from flask_mysqldb import MySQL

#Inicializacion del APP
app= Flask (__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='dbflask'
app.secret_key= 'mysecrety'
mysql= MySQL(app)

#Declaracion de ruta http://localhost:5000
@app.route('/')
def index():
  
  return render_template('index.html')

#rura http:localhost:5000/guardar tipo POST para insert
@app.route('/guardar',methods=['POST'])
def guardar():
  if request.method == 'POST':

    # pasamos a variables el contenido de los input
    Vtitulo=request.form['txtTitulo']
    Vartista=request.form['txtArtista']
    Vanio=request.form['txtAnio']
   
    #Conectar y ejecutar el insert
    cs= mysql.connection.cursor()
    cs.execute('insert into tbAlbums (titulo,artista,anio) values(%s,%s,%s)',(Vtitulo,Vartista,Vanio))
    mysql.connection.commit()

  flash('El album fue agregado correctamente')
  return redirect(url_for('index'))

@app.route('/eliminar')
def eliminar():
  
  return "Se elimino en la BD"

#Ejecucion del servidor en el puerto 5000
if __name__ == '__main__':
  app.run(port=5000,debug=True)

