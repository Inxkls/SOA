import mysql.connector
from mysql.connector import Error

def get_db_connection():
    """Establishes a connection to the MySQL database."""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='db_calificaciones', # Base de datos unificada
            user='root',      # Cambia esto por tu usuario
            password='Leones1320'       # Cambia esto por tu contraseña
        )
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

def init_db():
    """Initializes the database table if it does not exist."""
    # Primero intentamos conectar sin especificar base de datos para crearla si no existe
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Leones1320'
        )
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS db_calificaciones")
            print("Database 'db_calificaciones' checked/created.")
            cursor.close()
            connection.close()
    except Error as e:
        print(f"Error creating database: {e}")

    # Ahora conectamos a la base de datos y creamos la tabla
    connection = get_db_connection()
    if connection and connection.is_connected():
        try:
            cursor = connection.cursor()
            create_table_query = """
            CREATE TABLE IF NOT EXISTS inscripcion (
                id INT AUTO_INCREMENT PRIMARY KEY,
                estudiante_id VARCHAR(255) NOT NULL,
                curso_id VARCHAR(255) NOT NULL,
                fecha_inscripcion DATE NOT NULL
            )
            """
            cursor.execute(create_table_query)
            connection.commit()
            print("Table 'inscripcion' checked/created successfully.")
        except Error as e:
            print(f"Error creating table: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

if __name__ == '__main__':
    init_db()
