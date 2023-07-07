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









if __name__ == '__main__':
  app.run(port=5000,debug=True)