#importacion del framework
from flask import Flask, render_template, request,redirect,url_for,flash
from flask_mysqldb import MySQL

#Inicializacion del APP
app= Flask (__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='Medicos'
app.secret_key= 'mysecrety'
mysql= MySQL(app)

#Declaracion de ruta http://localhost:5000
@app.route('/')
def bienvenida():
  
  return render_template('bienvenida.html')


@app.route('/medico.html')
def medico():
  
  return render_template('medico.html')

@app.route('/paciente.html')
def paciente():
  
  return render_template('/pacientes.html')





@app.route('/medicos',methods=['POST'])
def medicos():
  if request.method == 'POST':

    # pasamos a variables el contenido de los input
    Vnombre=request.form['txtNombre']
    Vapellidop=request.form['textAp']
    Vapellidom=request.form['txtAm']
    Vrfc=request.form['textRFC']
    Vcorreo=request.form['txtCorreo']
    Vcontraseña=request.form['textcontrasena']
    Vrolid=request.form['txtid_rol']

    #Conectar y ejecutar el insert
    cs= mysql.connection.cursor()
    cs.execute('insert into medicos (nombre,ap,am,rfc,correo_electronico,contraseña,id_rol) values(%s,%s,%s,%s,%s,%s,%s)',(Vnombre,Vapellidop,Vapellidom,Vrfc,Vcorreo,Vcontraseña,Vrolid))
    mysql.connection.commit()

  flash('Se agrego correctamente')
  return redirect(url_for('medico'))



@app.route('/pacientes',methods=['POST'])
def pacientes():
    if request.method == 'POST':
        #pasamos a variables el contenido de los input
        Vnombrep=request.form['Nombrep']
        Vapellidop=request.form['Apellidop']
        Vapellidom=request.form['Apellidom']
        Vfecha=request.form['fecha']
        Vec=request.form['EC']
        Vnombremedico=request.form['Nombremedico']
    
        #conectar y ejecutar el insert
        CS= mysql.connection.cursor()
        CS.execute('insert into expedientes_pacientes(nombre,ap,am,fecha_nacimiento,enfermedades,id_medico) values(%s,%s,%s,%s,%s,%s)',(Vnombrep,Vapellidop,Vapellidom,Vfecha,Vec,Vnombremedico))
        mysql.connection.commit()
        
    flash('EL Registro fue guardado exitosamente')
    return redirect(url_for('paciente'))






#Ejecucion del servidor en el puerto 5000
if __name__ == '__main__':
  app.run(port=5000,debug=True)
