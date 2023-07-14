from flask import Flask, render_template, request,redirect,url_for,flash
from flask_mysqldb import MySQL

app= Flask (__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='DB_Floreria'
app.secret_key= 'mysecrety'
mysql= MySQL(app)

@app.route('/')
def index():
  
  return render_template('index.html')



@app.route('/registros.html')
def registros():
  CC= mysql.connection.cursor();
  CC.execute('select * from tbFlores')
  conFlor= CC.fetchall()
  print(conFlor)
  return render_template('registros.html',listflor= conFlor)



@app.route('/guardar',methods=['POST'])
def guardar():
  if request.method == 'POST':

   
    Vnombre=request.form['Flor']
    Vcantidad=request.form['Cantidad']
    Vprecio=request.form['Precio']
   
    
    cs= mysql.connection.cursor()
    cs.execute('insert into tbFlores (Nombre,cantidad,precio) values(%s,%s,%s)',(Vnombre,Vcantidad,Vprecio))
    mysql.connection.commit()

  flash('La flor fue registrada correctamente')
  return redirect(url_for('index'))



@app.route('/editar/<id>')
def editar(id):
  
  CID=mysql.connection.cursor();
  CID.execute('Select * from tbFlores where id=%s', (id))
  consultaID= CID.fetchone()
  return render_template('editar.html',flor=consultaID)



@app.route('/actualizar/<id>', methods=['POST'])
def actualizar(id):

  if request.method == 'POST':
    Vnombre=request.form['Flor']
    Vcantidad=request.form['Cantidad']
    Vprecio=request.form['Precio']
    
    curAct=mysql.connection.cursor()
    curAct.execute('update tbFlores set Nombre=%s, cantidad=%s, precio=%s where id=%s',(Vnombre, Vcantidad, Vprecio, id))
    mysql.connection.commit()
  
  flash('Se actualizo la flor'+ Vnombre)
  return redirect(url_for('registros'))



@app.route("/consulta.html")
def consulta():
    return render_template('consulta.html')



@app.route("/consulta")
def consulta():
    vflor = request.form.get('Flor', False)
    cs = mysql.connection.cursor()
    cs.execute('select * from tbFlores where Nombre = %s order by Nombre', [vflor])
    data = cs.fetchone()
    print(data)
    return render_template('consulta.html', flor = data)



if __name__ == '__main__':
  app.run(port=5000,debug=True)