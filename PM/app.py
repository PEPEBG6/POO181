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


@app.route('/')
def login():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(port=2000, debug=True)