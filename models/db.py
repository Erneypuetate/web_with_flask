import mysql.connector
from models.user import User

# Configuración de la conexión a la base de datos
config = {
  'user': 'example_user',
  'password': 'example_password',
  'host': 'mysql',
  'database': 'erney',
}
print(config)

def create_table(config):
    connection = mysql.connector.connect(**config)
    if connection.is_connected():
        print('Conexión exitosa a la base de datos MySQL')

        # Crea un cursor para ejecutar consultas
        with connection.cursor() as cursor:
            cursor.execute('''
                    CREATE TABLE IF NOT EXISTS users (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    username VARCHAR(100) NOT NULL,
                    password VARCHAR(100) NOT NULL,
                    email VARCHAR(100) NOT NULL
                    )
                ''')
            connection.commit()
        print("table created soccessful")
    else:
        print('table not create')

create_table(config)

def validate_user(config, name, password):
    connection = mysql.connector.connect(**config)
    if connection.is_connected():
        with connection.cursor() as cursor:
            sql = """SELECT id, username, password, email FROM users 
                    WHERE username = '{}'""".format(name)
            cursor.execute(sql)
            rows = cursor.fetchall()
        if rows==None:
            print('usuario no encontrado')
            return None
        else:
            for row in rows:
                user=User(row[0], row[1], row[2],row[3])
                if user.checkPassword(row[2],password):
                    print('contraseña correcta')
                    return user
                else:
                    print('contraseña incorrecta')
                    return False

    else: 
        return 'no hay conneccion'

def crete_user(config, name, password, email ):
    connection = mysql.connector.connect(**config)
    if connection.is_connected():
        with connection.cursor() as cursor:
            sql = """INSERT INTO users
             (username, password, email) 
             VALUES ('{}', '{}', '{}');
            """.format(name,password, email)
            cursor.execute(sql)
        connection.commit()
        print('datos insertados')
        return True
    else:
        print('datos no insertados')
        return False

def get_user_by_id(config, id):
    connection = mysql.connector.connect(**config)
    if connection.is_connected():
        with connection.cursor() as cursor:
            sql = """SELECT id, username, password, email FROM users 
                    WHERE id = '{}'""".format(id)
            cursor.execute(sql)
            row = cursor.fetchone()
        connection.commit()
        return User(row[0], row[1], row[2],row[3])
    else:
        return None




