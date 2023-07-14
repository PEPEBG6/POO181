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

 


if __name__ == '__main__':
  app.run(port=5000,debug=True)