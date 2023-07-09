from flask import Flask, render_template, request,redirect,url_for,flash
from flask_mysqldb import MySQL


app= Flask (__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='DB_Fruteria'
app.secret_key= 'mysecrety'
mysql= MySQL(app)



@app.route('/')
def index():
  
  return render_template('index.html')



@app.route('/registros.html')
def registros():
  CC= mysql.connection.cursor();
  CC.execute('select * from tbFrutas')
  conFrut= CC.fetchall()
  print(conFrut)
  return render_template('registros.html',listfrut= conFrut)



@app.route('/guardar',methods=['POST'])
def guardar():
  if request.method == 'POST':

    
    Vfruta=request.form['Fruta']
    Vtemporada=request.form['Temporada']
    Vprecio=request.form['Precio']
    Vstock=request.form['Stock']
   
    
    cs= mysql.connection.cursor()
    cs.execute('insert into tbFrutas (fruta,temporada,precio,stock) values(%s,%s,%s,%s)',(Vfruta,Vtemporada,Vprecio, Vstock))
    mysql.connection.commit()

  flash('La fruta fue registrada correctamente')
  return redirect(url_for('index'))



@app.route('/editar/<id>')
def editar(id):
  
  CID=mysql.connection.cursor();
  CID.execute('Select * from tbFrutas where id=%s', (id))
  consultaID= CID.fetchone()
  return render_template('editarFruta.html',frut=consultaID)



@app.route('/actualizar/<id>', methods=['POST'])
def actualizar(id):

  if request.method == 'POST':
    Vfruta=request.form['Fruta']
    Vtemporada=request.form['Temporada']
    Vprecio=request.form['Precio']
    Vstock=request.form['Stock']

    curAct=mysql.connection.cursor()
    curAct.execute('update tbFrutas set fruta=%s, temporada=%s, precio=%s, stock=%s where id=%s',(Vfruta, Vtemporada, Vprecio, Vstock, id))
    mysql.connection.commit()
  
  flash('Se actualizo la fruta'+ Vfruta)
  return redirect(url_for('registros'))



@app.route('/eliminar/<id>')
def eliminar(id):

  CID=mysql.connection.cursor();
  CID.execute('Select * from tbFrutas where id=%s', (id))
  eliminarID= CID.fetchone()
  return render_template('eliminarFruta.html',frut=eliminarID)



@app.route('/borrar/<id>', methods=['POST'])
def borrar(id):

  if request.method == 'POST':
    
    curElim=mysql.connection.cursor()
    curElim.execute('delete from tbFrutas where id=%s',(id))
    mysql.connection.commit()
  
  flash('Se elimino la fruta')
  return redirect(url_for('registros'))



@app.route("/consultasFrutas.html")
def consultasFrutas():
    return render_template('consultasFrutas.html')



@app.route("/consulta")
def consulta():
    vfrutas = request.form.get('Fruta', False)
    cs = mysql.connection.cursor()
    cs.execute('select * from tbFrutas where fruta = %s order by fruta', [vfrutas])
    data = cs.fetchone()
    print(data)
    return render_template('consultasFrutas.html', frut = data)





if __name__ == '__main__':
  app.run(port=5000,debug=True)