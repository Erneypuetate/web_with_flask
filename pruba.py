import mysql.connector

def ping_mysql_container(host, port, user, password, database):
    try:
        # Establece la conexión a la base de datos MySQL
        connection = mysql.connector.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database
        )

        if connection.is_connected():
            print("Conexión exitosa a la base de datos MySQL")
            # Realiza una consulta simple para verificar la conexión
            cursor = connection.cursor()
            cursor.execute("SELECT 1")
            result = cursor.fetchone()
            print("Ping exitoso:", result)
            cursor.close()
            connection.close()
    except mysql.connector.Error as error:
        print("Error al conectarse a la base de datos MySQL:", error)

# Llama a la función ping_mysql_container con los parámetros adecuados
ping_mysql_container('localhost', '3306', 'example_user', 'example_password', 'erney')
