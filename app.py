from flask import Flask, render_template,request, redirect, url_for, flash
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, login_user, logout_user, login_required, current_user

from models.db import create_table, validate_user, config, crete_user, get_user_by_id
from models.user import User
from flask_mysqldb import MySQL
import mysql.connector
 

app = Flask(__name__)
#app.config.from_object(Config)
#db =MySQL(app)

app.secret_key = "mysecretkey"

csrf = CSRFProtect()

login_manager_app = LoginManager(app)



#create_table(db)
@login_manager_app.user_loader
def load_user(id):
    return get_user_by_id(config, id)



@app.route("/")
def index():
    return redirect(url_for('login'))

@app.route("/home")
@login_required
def home():
    if current_user.is_authenticated:
        user_id = current_user.id
    # Continuar con la lógica que requiere el ID del usuario
    else:
        print('not uthentify')
    return render_template("home.html", user=current_user)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method=='POST':
        print(request.form['username'])
        print(request.form['password'])
        name=request.form['username']
        password=request.form['password']
        if validate_user(config, name, password)==None:
            flash('incorrect user')
            return redirect(url_for('login'))
        elif validate_user(config, name, password)==False:
            flash('incorrect password')
            return redirect(url_for('login'))
        else:
            user=validate_user(config, name, password)
            login_user(user)
            return redirect(url_for('home'))
    else:
        return render_template("index.html")

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method=='POST':
        print(request.form['username'])
        print(request.form['password'])
        print(request.form['email'])
        name=request.form['username']
        password=request.form['password']
        email=request.form['email']
        if crete_user(config, name, password, email):
            flash('usuario creado correctamente')
            return redirect(url_for('login'))
    return render_template("register.html")


if __name__=='__main__':
    #app.config.from_object(config['development'])
    app.run(debug=True)