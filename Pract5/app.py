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
  CC= mysql.connection.cursor();
  CC.execute('select * from tbAlbums')
  conAlbums= CC.fetchall()
  print(conAlbums)
  return render_template('index.html',listAlbums= conAlbums)

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


@app.route('/editar/<id>')
def editar(id):
  
  CID=mysql.connection.cursor();
  CID.execute('Select * from tbAlbums where id=%s', (id))
  consultaID= CID.fetchone()
  return render_template('editarAlbum.html',album=consultaID)


@app.route('/actualizar/<id>', methods=['POST'])
def actualizar(id):

  if request.method == 'POST':
    varTitulo=request.form['txtTitulo']
    varArtista=request.form['txtArtista']
    varAnio=request.form['txtAnio']

    curAct=mysql.connection.cursor()
    curAct.execute('update tbAlbums set titulo=%s, artista=%s, anio=%s where id=%s',(varTitulo, varArtista, varAnio, id))
    mysql.connection.commit()
  
  flash('Se actualizo el album'+ varTitulo)
  return redirect(url_for('index'))



@app.route('/eliminar/<id>')
def eliminar(id):

  CID=mysql.connection.cursor();
  CID.execute('Select * from tbAlbums where id=%s', (id))
  eliminarID= CID.fetchone()
  return render_template('eliminarAlbum.html',album=eliminarID)


@app.route('/borrar/<id>', methods=['POST'])
def borrar(id):

  if request.method == 'POST':
    
    curElim=mysql.connection.cursor()
    curElim.execute('delete from tbAlbums where id=%s',(id))
    mysql.connection.commit()
  
  flash('Se elimino el album')
  return redirect(url_for('index'))


#Ejecucion del servidor en el puerto 5000
if __name__ == '__main__':
  app.run(port=5000,debug=True)

